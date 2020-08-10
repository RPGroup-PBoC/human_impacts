var hover_ind = cb_data.index.indices;
var hover_year = animal_source.data['year'][hover_ind];
var donut_display = frac_source.data;
var barnyard_display = barnyard_source.data;

// Get all indices that match the selected year. 
cat_inds = getAllIndexes(cat_source.data['year'], hover_year);

// Update the display source. 
if (hover_year.length != 1) { 
donut_display['angle'] = [];
donut_display['category'] = [];
donut_display['fraction'] = [];
donut_display['pop_total'] = [];
donut_display['color'] = [];
donut_display['label'] = [];
donut_display['year'] = []

for (var i = 0; i < cat_inds.length; i++) { 
    donut_display['year'].push(hover_year);
    donut_display['angle'].push(cat_source.data['angle'][cat_inds[i]]);
    donut_display['category'].push(cat_source.data['category'][cat_inds[i]]);
    donut_display['pop_total'].push(cat_source.data['pop_total'][cat_inds[i]]);
    donut_display['fraction'].push(cat_source.data['fraction'][cat_inds[i]]);
    donut_display['color'].push(cat_source.data['color'][cat_inds[i]]);
    donut_display['label'].push(cat_source.data['label'][cat_inds[i]]);
}
frac_source.change.emit();

animal_inds = getAllIndexes(animal_source.data['year'], hover_year);
barnyard_display['barnyard_number'] = [];
barnyard_display['animal'] = [];
barnyard_display['color'] = [];
barnyard_display['year'] = [];
for (var i = 0; i < animal_inds.length; i++) { 
    barnyard_display['barnyard_number'].push(animal_source.data['barnyard_number'][animal_inds[i]]);
    barnyard_display['animal'].push(animal_source.data['animal'][animal_inds[i]]);
    barnyard_display['color'].push(animal_source.data['color'][animal_inds[i]]);
    barnyard_display['year'].push(hover_year);
}
barnyard_source.change.emit();
}

