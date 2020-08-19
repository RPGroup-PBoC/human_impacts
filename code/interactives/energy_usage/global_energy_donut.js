// Identify the hovered year
var year = year_slider.value;
// Find the indices of the hover
year_inds = getAllIndexes(power_source.data['year'], year);

// UPdate the display source
donut_display.data['total_angle'] = [];
donut_display.data['total_frac_label'] = [];
donut_display.data['total_label'] = [];
donut_display.data['capita_angle'] = [];
donut_display.data['capita_frac_label'] = [];
donut_display.data['capita_label'] = [];
donut_display.data['type'] = [];
donut_display.data['color'] = [];

for (var i = 0; i < year_inds.length; i++) {
    donut_display.data['year'].push(year);
    donut_display.data['total_angle'].push(power_source.data['total_angle'][year_inds[i]]);
    donut_display.data['capita_angle'].push(power_source.data['capita_angle'][year_inds[i]]);
    donut_display.data['total_frac_label'].push(power_source.data['total_frac_label'][year_inds[i]]);
    donut_display.data['capita_frac_label'].push(power_source.data['capita_frac_label'][year_inds[i]]);
    donut_display.data['total_label'].push(power_source.data['total_label'][year_inds[i]]);
    donut_display.data['capita_label'].push(power_source.data['capita_label'][year_inds[i]]);
    donut_display.data['type'].push(power_source.data['type'][year_inds[i]]);
    donut_display.data['color'].push(power_source.data['color'][year_inds[i]]);
}
donut_display.change.emit();
console.log(donut_display.data)
// Custom Function Definitions
function getAllIndexes(arr, val) {
    var indices = [], i = -1;
    while ((i = arr.indexOf(val, i+1)) != -1){
        indices.push(i);
    }
    return indices;
}
