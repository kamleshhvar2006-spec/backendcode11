// Toggle a task's done state without reloading the page.
(function () {
  var csrf = document.querySelector('meta[name="csrf-token"]').content;
  var counter = document.getElementById("open-count");

  document.querySelectorAll(".toggle").forEach(function (box) {
    box.addEventListener("change", function () {
      var row = box.closest(".item");
      fetch(box.dataset.url, {
        method: "POST",
        headers: { "X-CSRFToken": csrf },
      })
        .then(function (res) {
          if (!res.ok) throw new Error("Request failed");
          return res.json();
        })
        .then(function (data) {
          row.classList.toggle("is-done", data.done);
          box.checked = data.done;
          if (counter) counter.textContent = data.open_count;
        })
        .catch(function () {
          box.checked = !box.checked; // revert on failure
          alert("Could not update the task. Check your connection and try again.");
        });
    });
  });
})();
