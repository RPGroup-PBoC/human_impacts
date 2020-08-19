// Define data sources and interaction variables
var year = year_slider.value;
var cat_donut = cat_display.data;
var cat_data = cat_source.data;
var animal_stick = animal_display.data;
var animal_data = animal_source.data;

// Find the indices for both the animal data and the category data
var animal_inds = getAllIndexes(animal_data['year'], year);
var cat_inds = getAllIndexes(cat_data['year'], year);


// Update the display data for the cat inds first. 
for (var i = 0; i < cat_inds.length; i++) {
    if (i == 0) {
        cat_donut['year'] = [];
        cat_donut['angle'] = [];
        cat_donut['human_pop'] = [];
        cat_donut['category'] = [];
        cat_donut['cat_pop'] = [];
        cat_donut['capita'] = []
        cat_donut['frac_label'] = [];
        cat_donut['frac'] = [];
        cat_donut['color'] = [];
    }

    cat_donut['year'].push(cat_data['year'][cat_inds[i]]);
    cat_donut['angle'].push(cat_data['angle'][cat_inds[i]]);
    cat_donut['human_pop'].push(cat_data['human_population'][cat_inds[i]]);
    cat_donut['capita'].push(cat_data['capita'][cat_inds[i]]);
    cat_donut['cat_pop'].push(cat_data['pop_total'][cat_inds[i]]);
    cat_donut['frac_label'].push(cat_data['frac_label'][cat_inds[i]]);
    cat_donut['frac'].push(cat_data['fraction'][cat_inds[i]]);
    cat_donut['category'].push(cat_data['category'][cat_inds[i]]);
    cat_donut['color'].push(cat_data['color'][cat_inds[i]]);
} 
cat_display.change.emit();

// Update the display data for the animal inds
for (var i = 0; i < animal_inds.length; i++) {
    if (i == 0) {
        animal_donut['year'] = [];
        animal_donut['human_pop'] = [];
        animal_donut['animal_pop'] = [];
        animal_donut['capita'] = []
        animal_donut['frac'] = [];
        animal_donut['animal'] = [];
        animal_donut['color'] = [];
    }

    animal_donut['year'].push(animal_data['year'][animal_inds[i]]);
    animal_donut['human_pop'].push(animal_data['human_population'][animal_inds[i]]);
    animal_donut['capita'].push(animal_data['capita'][animal_inds[i]]);
    animal_donut['animal_pop'].push(animal_data['pop_total'][animal_inds[i]]);
    animal_donut['frac'].push(animal_data['fraction'][animal_inds[i]]);
    animal_donut['animal'].push(animal_data['animal'][animal_inds[i]]);
    animal_donut['color'].push(animal_data['color'][animal_inds[i]]);
} 
animal_display.change.emit();

function getAllIndexes(arr, val) {
    var indices = [], i = -1;
    while ((i = arr.indexOf(val, i+1)) != -1){
        indices.push(i);
    }
    return indices;
}