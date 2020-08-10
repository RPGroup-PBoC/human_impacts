var cat = cat_select.value;
var pop_display = pop_display_source.data;
var prod_display = prod_display_source.data;

// Get the indices of the selected category
inds = getAllIndexes(cat_source.data['primary'], cat)

// Reset population plot
pop_display['year'].length = 0;
pop_display['producing_population_Mhd'].length = 0;
pop_display['pop_total'].length = 0;
pop_display['color'].length = 0;
pop_display['secondary'].length = 0;
pop_display['primary'].length = 0;

// Reset production plot
prod_display['year'].length = 0;
prod_display['produced_Mt'].length = 0;
prod_display['prod_total'].length = 0;
prod_display['color'].length = 0;
prod_display['secondary'].length = 0;
prod_display['primary'].length = 0;


for (var i = 0; i < inds.length; i++) {
    // Update population plot
    pop_display['year'].push(cat_source.data['year'][inds[i]]);
    pop_display['producing_population_Mhd'].push(cat_source.data['producing_population_Mhd'][inds[i]]);
    pop_display['pop_total'].push(cat_source.data['pop_format'][inds[i]]);
    pop_display['color'].push(cat_source.data['color'][inds[i]]);
    pop_display['secondary'].push(cat_source.data['secondary'][inds[i]]);
    pop_display['primary'].push(cat);

    // Update the production plot
    prod_display['year'].push(cat_source.data['year'][inds[i]]);
    prod_display['produced_Mt'].push(cat_source.data['produced_Mt'][inds[i]]);
    prod_display['prod_total'].push(cat_source.data['prod_format'][inds[i]]);
    prod_display['color'].push(cat_source.data['color'][inds[i]]);
    prod_display['secondary'].push(cat_source.data['secondary'][inds[i]]);
    prod_display['primary'].push(cat);
}

// Emit the changes. 
pop_display_source.change.emit();
prod_display_source.change.emit();
