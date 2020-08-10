var animal = animal_select.value;

// Get all indices of the selected animal:
inds = getAllIndexes(animal_source.data['animal'], animal);
animal_filter.indices = inds;
animal_view.filters[0] = animal_filter;
animal_source.data.view = animal_view;
animal_source.change.emit();

