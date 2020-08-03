### Livestock by the Numbers -- Population
Any drive through the countryside, flight over the heartland of the central
United States, or stroll through your local grocer will lead you to the same
conclusion -- a large amount of resources are dedicated to the rearing of
animals as a protein source. In general, $\approx$ 30\% of the typical American
diet is derived from animal products [@eshel2014] with the remainder coming from
various crops which we will consider in depth later in this vignette. 

Since 1961, the Food and Agriculture Organization (FAO) of the United Nations
has kept track of myriad data reflecting the extent, efficiency, and changes in
global crop and livestock production. A key statistic tracked by the FAO is the
global standing population of a wide variety of livestock. Collected at
approximately the same time per year per reporting country, these data, 
portrayed graphically in @Fig:standing_pop_distribution (A), reflects a
snapshot of how many animals livestock are under human agricultural maintenance.
Chicken, both egg-laying and meat-producing varieties, are far and away the most
abundant type of livestock on the planet with $\approx$ 20 billion individuals
under human care. Second to chicken are cattle, comprising approximately one
tenth that of the chicken population at $\approx$ 2 billion individuals.
Following cattle are swine at $\approx$ 1 billion individuals and then all other
types of livestock (including horses, other poultry fowl, sheep, goats, and
others) in total representing $\approx$ 6 billion individuals. Taking this data
together, there are on the order of $\approx$ 30 billion animals under the
umbrella of agriculture.

It is important to note, however, that this number does not reflect the
magnitude of human animal usage and rather represents the instantaneous animal
burden that humans must be able to support. Poultry chicken, for example, have a
remarkably short lifespan of $\approx$ 6 weeks from hatching to slaughter. With
such a rapid generation time (courtesy of decades of artificial selection for
fast-growing variants), the entire standing population could be exchanged
$\approx$ 8 times per year. Conversely, cattle have a typical lifespan of a few
years from birth to slaughter, meaning that the observed standing population is
larger than that actually processed and consumed each year. 


![**The population and biomass distribution of livestock on Earth.** The species breakdown
of livestock is shown in terms of global population based on the average from years 2010 - 2018
present in the FAOSTAT livestock database. Category of "other" includes asses and
mules, beehives, buffalo, camels and camelids, duck, geese and guinea fowl,
goats, horses, pigeons and other small fowl, rabbits, rodents, sheep, and turkey.
estimates listed in Table. A1.](figures/standing_pop.pdf){#fig:standing_pop}


While these numbers are striking, can we make sense of them? In the coming
sections, we will perform a series of estimates to see of the observed order of
magnitude of population jibes with simple expectations based on a typical human
dietary breakdown. We will explore our estimates in more detail using additional
data from the FAO which tracks the mass of animal product produced per year as
well as the number of animals processed and/or slaughtered to produce said
product.


#### What is the typical diet?
The specifics of human dietary requirements and their actual realizations is a
very active field of research, and can be rather controversial. Regional diets
can be remarkably diverse, making it difficult to think of the "average" diet.
However, for convenience, we will make an approximation that the typical diet is
something comparable to a typical Western diet, at least to within a factor of a
few.


Recent work has painstakingly and carefully estimated the typical American diet
that arises fro 



#### Chicken 

We begin our estimates with the most abundant livestock species by number --
chicken. As noted in our discussion earlier (see FIG XXX), our typical human
will consume $\approx$ 1\% of their daily caloric intake from from
chicken-derived eggs. To put this number in context, let's assume that the
typical person consumes $\approx$ one-half dozen eggs per week. With $\approx$
50 kcal per egg, this comes to a total of $\approx$ 300 kcal per week, which is
$\approx$ 2\% of a weekly caloric requirement of 14,000 kcal. Given that on
one-half dozen eggs per week may be a bit of an over estimate by a factor of
$\approx$ a few, we can feel moderately confident that an estimate of 1\% is
fair for the typical caloric contribution of eggs. 

With a mass of $\approx$ 50 grams per egg and our previous assertion of
$\approx$ 50 kcal per egg, we arrive at a caloric density of $\approx$ 1
kcal $\cdot$ g$^{-1}$ of egg consumed. Given this number we can quickly arrive at
an estimate that the typical human has to eat around one egg every other day or so.
Coupled with a global population of $\approx 7 \cdot 10^{9}$ people on the
planet, and 365 days per year, we can compute an estimated yearly mass of
consumed eggs to be $\approx 5 \cdot$10$^{10}$ kg  or $\approx$ 50
Mt $\cdot$ year$^{-1}$.  This estimate, schematized in the top-panel of
@Fig:chicken_estimate (A) is well within a factor of two of the actual mass
produced per year. Over the 2010-2018 year period of data collected by the FAO,
there were on average $\approx$ 65 Mt of eggs produced per year. This, for
reference, corresponds to $\sim$ 10$^{12}$ eggs or $\sim$ 100 billion cartons of
eggs. 

How does this compare to poultry, the other potential fate of chicken? Again
relying on the work of @eshel2014, poultry is responsible for $\approx$ 5\% of
the typical caloric input or $\approx$ 100 kcal per day. The caloric density of
poultry meat depends on the type of cut (dark meat or light meat), but for
purposes we will make the approximation that it is similar to that of eggs or
$\approx$ 1 kcal $\cdot$ g$^{-1}$. This means that per day, our typical person must
consume $\approx$ 100 g or poultry per day. Following the procedure shown in the
bottom panel of @Fig:chicken_estimate (A), we arrive at an estimate of $\sim$
3$\sim$ 10$^{11}$ kg or $\sim$ 300 Mt per year. This number is within a factor
of a few of the 2010-2018 FAO average of $\sim$ 1000 Mt per year, a difference
reasonable considering our approximation of the typical diet be similar the
Western diet. 

These estimates represent a reasonable order-of-magnitude argument for the total
mass of *consumed* egg and poultry. It it interesting that these numbers are
closely aligned with the FAO measurements of the globally *produced* mass.
The typical fraction of food lost due to waste (spoilage or
plate-to-trashcan loss) is $\approx$ 20\% [@shepon2018], providing a somewhat
reasonable estimate of our error or general uncertainty of these estimates.


How many animals are responsible for producing this rather incredible mass?
While tempting, it is *not* a reasonable assumption to state that all chickens
are the same. Typically, the breeds of chicken used to produce eggs have
little-to-no overlap with the chicken breasts that decorate our grocery's
coolers. Egg-producing chickens, colloquially termed "layer" chickens, typically
live around 18 months and are able to begin laying eggs as early as four months
of age. With a laying rate of $\approx$ 1 egg $\cdot$ day$^{-1}$, the high-yield
layer chicken can produce $\approx$ 350 eggs $\cdot$ year$^{-1}$ [@zaheer2015]. We
will, for the sake of convenience, that all chickens globally operate at this
high-yield. Again assuming a typical egg mass of $\approx$ 50 g, we arrive at an
estimate of $\approx 3 \times 10^9$ layer chickens needed to produce the
estimated annual mass of eggs produced globally. This estimate is very close to
the FAO observed average of $\approx 7 \times 10^9$ layer chickens per year.
Given that our approximation of all chickens as high-yield, 300 egg per year
producing varieties, we expect our value to be a mild underestimate of the
measured value. 

Meat-producing chicken, typically referred to as "broiler" chickens, have also
been the targets of intense industrial breeding to maximize yield. This variety
of chicken has a remarkably short life span of $\approx$ 6 weeks, during which
time they can accumulate $\approx$ 5 kg of body mass, a remarkable increase from
the $\approx$ 1 kg body mass of mature broiler chickens in the mid 1950's
[@zuidhof2014;@tallentire2016]. Of this body mass, $\approx$ 70\% is ultimately
harvested for human consumption and/or feed production [@kokoszynski2008]




 with another
$\approx$ 5\% coming directly from chicken meat, hereafter termed "poultry".
Given this breakdown, we can estimate the total mass of consumed  egg and
poultry, ultimately allowing us to estimate the number of animals processed for
this number. 


With a $\approx$ 2000 kcal$\cdot$day$^{-1}$ diet, 



![**Sizing up global mass of consumed chicken product and processed population.** (A) Estimate for the
amount of eggs (top panel) and poultry (bottom panel) consumed per year. The daily
caloric intake of the average human is assumed to be $\approx$ 2000 kcal $\cdot$
day$^{-1}$. (B) Estimate for the number of processed chickens per year to produce 
mass of egg and poultry from estimates in (A). Donut charts in right-hand side
show the average distribution of chicken product (top) and processed chicken population
(bottom) from the years 2010-2018 as recorded in the FAOSTAT data base. Reported
values for total mass and processed population is reported as the mean and
standard deviation of the 2010-2018 measurements.](figures/chicken_production_estimate.pdf){#fig:chicken_estimate}

#### Cattle

![**Sizing up global mass of consumed cow product and processed population.** (A) Estimate for the
amount of milk (top panel) and beef (bottom panel) consumed per year. The daily
caloric intake of the average human is assumed to be $\approx$ 2000 kcal $\cdot$
day$^{-1}$. (B) Estimate for the number of processed cattle per year to produce 
mass of milk and dairy from estimates in (A). Donut charts in right-hand side
show the average distribution of cattle product (top) and processed cattle population
(bottom) from the years 2010-2018 as recorded in the FAOSTAT data base. Reported
values for total mass and processed population is reported as the mean and
standard deviation of the 2010-2018 measurements.](figures/cattle_production_estimate.pdf){#fig:cattle_estimate}



#### Swine

![**Sizing up global mass of consumed pork product and processed population.**
(A) Estimate for the mass of pork product produced. The daily caloric intake of
the average human is assumed to be $\approx$ 2000 kcal $\cdot$ day$^{-1}$. (B)
Estimate for the number pigs processed per year given pork product mass estimate
given in (A). Text-boxes on right-hand side of (A) and (B) correspond to the
mean and standard deviation of the reported measurements in the FAOSTAT data
base for the years 2010-2018.](figures/swine_production_estimate.pdf){#fig:pig_estimate}

#### The Magnitude of Annual Livestock Processing
![**Rules-of-thumb for the annual flux of processed animals per capita.**
Values provided in the number estimates correspond to the approximate averages
of the reported producing population for each product from the FAOSTAT database
for years 2010-2018. The "Farm-To-Table" number considers estimate of the number
of animals processed for all meat, milk, and egg production across several
animal categories as calculated by the FAO.](figures/livestock_processing_numbers.pdf){#fig:processing_numbers}