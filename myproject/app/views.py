from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ItemForm
from .models import Item


def item_list(request):
    """List items (with ?show=open|done filter) and create new ones."""
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm()

    show = request.GET.get("show", "all")
    items = Item.objects.all()
    if show == "open":
        items = items.filter(done=False)
    elif show == "done":
        items = items.filter(done=True)

    context = {
        "form": form,
        "items": items,
        "show": show,
        "open_count": Item.objects.filter(done=False).count(),
        "total_count": Item.objects.count(),
    }
    return render(request, "app/item_list.html", context)


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("item_list")
    return render(request, "app/item_form.html", {"form": form, "item": item})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("item_list")
    return render(request, "app/item_confirm_delete.html", {"item": item})


@require_POST
def item_toggle(request, pk):
    """Called by app.js when a checkbox is clicked. Returns JSON."""
    item = get_object_or_404(Item, pk=pk)
    item.done = not item.done
    item.save(update_fields=["done"])
    return JsonResponse({
        "done": item.done,
        "open_count": Item.objects.filter(done=False).count(),
    })


def api_items(request):
    """Read-only JSON API: /api/items/"""
    data = list(Item.objects.values("id", "title", "description", "done", "created_at"))
    return JsonResponse({"items": data})
