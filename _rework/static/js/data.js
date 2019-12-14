$('#City').on('change',function(){
  var selection = $(this).val();
  console.log("Detected change..." + selection);
  if (selection == "Cork"){
    $("#areasDublin").hide();
    $("#areasGalway").hide();
    $("#areasLimerick").hide();
    $("#areasCork").show();
    $("#areasEmpty").hide();
  }
  else if (selection == "Dublin"){
        $("#areasDublin").show();
        $("#areasGalway").hide();
        $("#areasLimerick").hide();
        $("#areasCork").hide();
        $("#areasEmpty").hide();
  }
    else if (selection == "Limerick"){
        $("#areasDublin").hide();
        $("#areasGalway").hide();
        $("#areasLimerick").show();
        $("#areasCork").hide();
        $("#areasEmpty").hide();
  }
    else {
        $("#areasDublin").hide();
        $("#areasGalway").show();
        $("#areasLimerick").hide();
        $("#areasCork").hide();
        $("#areasEmpty").hide();
  }

});






















