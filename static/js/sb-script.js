$(document).ready(function () {
  $(".btn-submit").click(function () {
    $("#selectBox :nth-child(0)").prop("selected", true);
    $("#selectBox :nth-child(1)").prop("selected", false);
    $("#selectBox :nth-child(2)").prop("selected", false);
    $("#selectBox :nth-child(3)").prop("selected", false);
  });

  $(".service_type")
    .change(function () {
      $(this)
        .find("option:selected")
        .each(function () {
          var optionValue = $(this).attr("value");
          if (optionValue) {
            $(".box")
              .not("." + optionValue)
              .hide();
            $("." + optionValue).show();
          } else {
            $(".box").hide();
          }
        });
    })
    .change();
});
