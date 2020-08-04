## Livestock by the Numbers -- Population
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
portrayed graphically in @Fig:standing_pop (A), reflects a
snapshot of how many animals livestock are under human agricultural maintenance.
Chicken, both egg-laying and meat-producing varieties, are far and away the most
abundant type of livestock on the planet with $\approx$ 20 billion individuals
under human care. Second to chicken are cattle, comprising approximately one
tenth that of the chicken population at $\approx$ 2 billion individuals.
Following cattle are swine at $\approx$ 1 billion individuals and then all other
types of livestock (including horses, other poultry fowl, sheep, goats, and
others) in total representing $\approx$ 6 billion individuals. Taking this data
together, there are on the order of $\approx$ 30 billion animals under the
umbrella of agriculture at any given point in time over the past decade.

It is important to note, however, that this number does not reflect the
magnitude of human animal usage and rather represents the instantaneous animal
burden that humans must be able to support. Poultry chicken, for example, have a
remarkably short lifespan of $\approx$ 6 weeks from hatching to harvest. With
such a rapid generation time, the entire standing population could be exchanged
$\approx$ 8 times per year. Conversely, cattle have a typical lifespan of a few
years from birth to slaughter, meaning that the observed standing population is
larger than that actually processed and consumed each year. 


![**The population distribution of livestock on Earth.** The species breakdown
of livestock is shown in terms of global population based on the average from years 2010 - 2018
present in the FAOSTAT livestock database. Category of "other" includes asses and
mules, beehives, buffalo, camels and camelids, duck, geese and guinea fowl,
goats, horses, pigeons and other small fowl, rabbits, rodents, sheep, and turkey.](figures/standing_pop.pdf){#fig:standing_pop}


While these numbers are striking, can we make sense of them? In the coming
sections, we will perform a series of estimates to see of the observed order of
magnitude of population jibes with simple expectations based on a typical human
dietary breakdown. We will explore our estimates in more detail using additional
data from the FAO which tracks the mass of animal product produced per year as
well as the number of animals processed and/or slaughtered to produce said
product.


### What is the typical diet?
![**The archetypal Western diet.** Partitioning of the daily caloric intake
between major animal sources is shown schematically on the left-hand side.
Right-hand side shows the caloric breakdown of categories shown on the left, with
one box representing $\approx$ 20 kcal and the sum of all boxes to be $\approx$
2000 kcal.](figures/western_diet.pdf){#fig:diet}


The specifics of human dietary requirements and their actual realizations is a
very active field of research, and can be rather controversial. Regional diets
can be remarkably diverse, making it difficult to think of the "average" diet.
However, for convenience, we will make an approximation that the typical diet is
something comparable to a standard Western diet, at least to within a factor of a
few. In particular, we will utilize recent characterizations of the typical Western
diet, depicted in @Fig:diet. While we will dive deeper into the details of the
non-plant component of the typical diet, we will take the animal-derived portion
to be $\approx$ 10\% dairy, 10\% beef, 5\% poultry,  5\% pork, and 1\% derived
from eggs.



[GC Note: Would like to do a more detailed take on the expected error of this
approximation. Can use FAO data to consider regional production export/import of
animal product to see how big of an error this is. ]


### Chicken 

We begin our estimates with the most abundant livestock species by number --
chicken. As noted in @Fig:diet, our typical human will consume $\approx$ 1\%
of their daily caloric intake from from chicken-derived eggs. To put this
number in context, let's assume that the typical person consumes $\approx$
one-half dozen eggs per week. With $\approx$ 50 kcal per egg, this comes to a
total of $\approx$ 300 kcal per week, which is $\approx$ 2\% of a weekly
caloric requirement of 14,000 kcal. Given that on one-half dozen eggs per
week may be a bit of an over estimate by a factor of $\approx$ a few, we can
feel moderately confident that an estimate of 1\% is fair for the typical
caloric contribution of eggs.

With a mass of $\approx$ 50 grams per egg and our assertion of
$\approx$ 50 kcal per egg, we arrive at a caloric density of $\approx$ 1
kcal $\cdot$ g$^{-1}$ of egg consumed. Given this number we can quickly arrive at
an estimate that the typical human has to eat around one egg every other day.
Coupled with a global population of $\approx 7 \cdot 10^{9}$ people on the
planet and 365 days per year, we can compute an estimated yearly mass of
consumed eggs to be $\approx 5 \cdot 10^{10}$ kg  or $\approx$ 50
Mt $\cdot$ year$^{-1}$.  This estimate, schematized in the top-panel of
@Fig:chicken_estimate (A) is well within a factor of two of the actual mass
produced per year. Over the 2010--2018 year period of data collected by the FAO,
there were on average $\approx$ 65 Mt of eggs produced per year. This, for
reference, corresponds to $\sim 10^{12}$ eggs or $\sim$ 100 billion cartons.


How does this compare to poultry, the other potential fate of chicken? Again
relying on the work of @eshel2014, poultry is responsible for $\approx$ 5\% of
the typical caloric input or $\approx$ 100 kcal per day. The caloric density of
poultry meat depends on the type of cut (dark meat or light meat), but for
purposes we will make the approximation that it is similar to that of eggs or
$\approx$ 1 kcal $\cdot$ g$^{-1}$. This means that per day, our typical human must
consume $\approx$ 100 g of poultry per day. Following the procedure shown in the
bottom panel of @Fig:chicken_estimate (A), we arrive at an estimate of $\sim
3\cdot 10^{11}$ kg or $\sim$ 300 Mt per year. This number is within a factor
of a few of the 2010-2018 FAO average of $\sim$ 1000 Mt per year, a difference
reasonable considering our approximation of the typical diet to be similar the
Western diet. 

These estimates represent a reasonable order-of-magnitude argument for the total
mass of *consumed* egg and poultry. It is interesting that these numbers are
closely aligned with the FAO measurements of the globally *produced* mass.
The typical fraction of food lost due to waste (spoilage or
plate-to-trashcan loss) is $\approx$ 20\% [@shepon2018], providing a somewhat
reasonable estimate of our error or general uncertainty of these estimates.


How many animals are responsible for producing this rather incredible mass?
While it is tempting, it is *not* a reasonable assumption to state that all chickens
are the same. Typically, the breeds of chicken used to produce eggs have
little-to-no overlap with the chicken breasts that decorate our grocery
coolers. Egg-producing chickens, colloquially termed "layer" chickens, typically
live around 18 months and are able to begin laying eggs as early as two months
of age. With a laying rate of $\approx$ 1 egg $\cdot$ day$^{-1}$, the high-yield
layer chicken can produce $\approx$ 350 eggs $\cdot$ year$^{-1}$ [@zaheer2015]. We
will, for the sake of convenience, that all chickens globally operate at this
high-yield. Again assuming a typical egg mass of $\approx$ 50 g, we arrive at an
estimate of $\approx 3 \cdot 10^9$ layer chickens needed to produce the
estimated annual mass of eggs produced globally. This estimate is very close to
the FAO observed average of $\approx 7 \cdot 10^9$ layer chickens per year.
Given that our approximation of all chickens as high-yield, 350 egg per year
producing varieties, we expect our value to be a mild underestimate of the
measured value. 

Meat-producing chicken, typically referred to as "broiler" chickens, have also
been the targets of intense industrial breeding to maximize yield. This variety
of chicken has a remarkably short life span of $\approx$ 6 weeks, during which
time they can accumulate $\approx$ 4 kg of body mass, a remarkable increase from
the $\approx$ 1 kg body mass of mature broiler chickens in the mid 1950's
[@zuidhof2014;@tallentire2016]. Of this body mass, $\approx$ 70\% is ultimately
harvested [@kokoszynski2008] yielding around $\approx$ 3 kg of edible mass per
broiler chicken. Combining this array of numbers, we can arrive at an estimate
(bottom panel of @Fig:chicken_estimate (B)) of $\sim 10^{11}$ broiler chicken
processed annually. Once again, this simple estimate is within a factor of a few
of the FAO recorded number of $\approx 6 \cdot 10^{11}$ broiler chicken per
year. This number dwarfs the number of layer chicken processed per year by
nearly an order of magnitude, even though the difference in produced mass is
only a factor of a few. 

Thus, on average, approximately $\approx$ 150 Mt of chicken product is produced
annual from $\approx$ 70 billion individuals. The latter value is larger than
the standing population by a factor of $\approx$ 4. We can remedy this apparent
disagreement by realizing that with a lifespan of $\approx \frac{1}{8}$ year,
the standing population can be computed as 
$$
N_\text{chicken}^\text{(standing pop.)} \approx \frac{70\cdot 10^9
\text{chicken}}{\text{year}}\cdot\frac{1}{8}\,\text{year} \approx 10^{10} \text{chickens},
$${#eq:chicken_standing_pop}
which is comparable to the $\approx 20 \cdot 10^9$ individuals reported by the
FAO and shown in @Fig:standing_pop.

![**Sizing up global mass of consumed chicken product and processed population.** (A) Estimate for the
amount of eggs (top panel) and poultry (bottom panel) consumed per year. The daily
caloric intake of the average human is assumed to be $\approx$ 2000 kcal $\cdot$
day$^{-1}$. (B) Estimate for the number of processed chickens per year to produce 
mass of egg and poultry from estimates in (A). Donut charts in right-hand side
show the average distribution of chicken product (top) and processed chicken population
(bottom) from the years 2010-2018 as recorded in the FAOSTAT data base. Reported
values for total mass and processed population is reported as the mean and
standard deviation of the 2010-2018 measurements.](figures/chicken_production_estimate.pdf){#fig:chicken_estimate}

### Cattle
With the population of chickens accounted for, we now turn our focus towards the
next abundant member of livestock -- cattle. Like chicken, cattle are
responsible for two major components of our typical human diet, dairy and beef.
The former includes milk which can be transformed into a variety of different 
foods such as cheese, butter, and curds, all of which make up $\approx$ 10\% of
daily calories or $\approx$ 200 kcal. As everything begins as milk, we will attempt to estimate the
total mass of cow milk produced annually. 

Full-fat milk has a relatively low caloric density of $\approx$ 0.5
kcal$\cdot$g$^{-1}$ ( @muehlhoff2013, pp. 107). Thus, with $\approx$ 200
kcal$\cdot$day$^{-1}$, around $\approx$ 200 g of milk need to be consumed per
person per day. It therefore follows that $\approx 10^{12}$ kg of milk are
consumed globally per year. Similarly to our estimates for chicken product, our
estimate for milk production is within a factor of a few from the measured
yearly production of $\approx 6\cdot10^{11}$ kg$\cdot$year$^{-1}$
(@Fig:cattle_estimate (A)).

Beef, like milk, also constitutes $\approx$ 10\% of daily calories in our
archetypal diet. However, beef is significantly more calorie dense than milk
with caloric density of $\approx$ 2 kcal$\cdot$g$^{-1}$ (GC note: according to
[http://calories.info](https://www.calories.info/), want to get this data from
USDA directly). Thus, to intake
$\approx$ 200 kcal$\cdot$day$^{-1}$, our typical human has to consume on the
order of 100 g of beef. As outlined in @Fig:cattle_estimate (A), expanding this
to the $\approx 7 \cdot 10^{9}$ people on the planet results in $\sim 10^{11}$
kg or $\sim$ 100 Mt a year. This estimate is within a factor of a few of the FAO
measurement of $\approx$ 60 Mt$\cdot$year$^{-1}$. 

How many cattle does it take to yield this amount of milk and beef? Like
chicken, cattle come in two varieties with dairy cattle producing milk and beef
cattle producing, well, beef. As each variety has been intensively bred to
prioritize milk or beef production, there is effectively zero overlap between
the producing populations. The exception is that dairy cattle, when exhausted of
their milk producing capacity, will be slaughtered for low-quality beef products
or high-protein feed for other livestock. For simplicity, we will assume that
the contribution of dairy cattle to yearly beef production is negligible. 

Dairy cattle are remarkable in their ability to produce milk. In industrial
settings, a high-yield dairy cow can produce around 30 L of milk per day or
$\approx$ 30 kg. This is produced over a maximum of $\approx$ 10 months with at
least 60-days of a rest period before lactation can resume. Thus, over a
$\approx$ 300 day lactation season, a single cow can produce $\approx 10^4$ kg
of milk -- an order of magnitude above what is typically produced in
non-industrial conditions [@bello2012]. With $\approx$ 10$^{12}$
kg milk $\cdot$year$^{-1}$, on the order of 10$^8$ dairy cattle are needed per
year, a value within  a factor of a few of the FAO measurement of $3 \cdot
10^8$.

What about for beef? Beef cattle have been bred to be enormous, with the typical
angus beef cattle being on the order of $\approx$ 500 - 1000 kg. This so-called
"on-the-hoof" mass is not completely edible. After slaughter, the carcass is
stripped of non-edible components resulting in a net edible mass of $\approx$
200 kg of beef per cow [@okffa2020a]. Therefore $\approx 5\cdot 10^8$
beef cattle are processed each year for beef, within a factor of two from the
FAO measurement of $\approx 3 \cdot 10^8$.

In total, $\approx$ 700 Mt of beef product is produced globally using $\approx$
550 million cattle. In contrast to the utilized chicken population, this number
is a factor of $\approx$ 3 *below* the FAO reported number for the standing
cattle population. This again is due to the matter of lifespan. Cattle, whether
beef or dairy, have a life span on the order of $\approx$ 2 - 3 years from birth
to culling. Thus, between 2 and 3 times the global processed population will
need to be reared per year to meet demand, meaning the standing population can
be approximated as 
$$
N_\text{cattle}^\text{(standing pop.)} \approx \frac{5.5 \cdot
10^8\,\text{cattle}}{\text{year}}\cdot 3\,\text{years} \approx 1.5 \cdot
10^9\text{cattle},
$${#eq:cattle_standing_pop}

which is inline with the $\approx 2 \cdot 10^8$ cattle under global agricultural
maintenance as reported by the FAO, shown in @Fig:standing_pop.

![**Sizing up global mass of consumed cow product and processed population.** (A) Estimate for the
amount of milk (top panel) and beef (bottom panel) consumed per year. The daily
caloric intake of the average human is assumed to be $\approx$ 2000 kcal $\cdot$
day$^{-1}$. (B) Estimate for the number of processed cattle per year to produce 
mass of milk and dairy from estimates in (A). Donut charts in right-hand side
show the average distribution of cattle product (top) and processed cattle population
(bottom) from the years 2010-2018 as recorded in the FAOSTAT data base. Reported
values for total mass and processed population is reported as the mean and
standard deviation of the 2010-2018 measurements.](figures/cattle_production_estimate.pdf){#fig:cattle_estimate}


### Swine
The final category of livestock animals we will explore via estimation here is
the population of swine. Unlike chicken and cattle, swine are primarily used for
a singular product, pork. To estimate the amount of pork consumed each year, we
again note that in our typical diet, pork makes up $\approx$ 5\% of daily
calories or $\approx$ 100 kcal. Like beef, pork is particularly calorie dense
with $\approx$ 2 kcal$\cdot$g$^{-1}$ (GC Note: again from calorie.info, need to
parse USDA data). As outlined in @Fig:pig_estimate (A), we arrive at an estimate
on the order of $\sim 10^8$ kg or $\approx$ 100 Mt of pork product per year.
This is in agreement with the FAO measurement of an average of $\approx 115$ Mt$\cdot$year$^{-1}$.

Typical pork swine will weigh close to around $\approx$ 100 kg at slaughter,
yielding a total of $\approx$ 70 kg of edible mass [@okffa2020]. Using our estimate of
$\approx$ 100 Mt of pork per year, we arrive at an estimate (@Fig:pig_estimate
(B)) that $\approx 2\cdot 10^9$ hogs are slaughtered each year, in line with the
average culling of $\approx 1.5 \cdot 10^9$ swine $\cdot$ year$^{-1}$ reported
by the FAO. 

Swine represent another category of livestock in which more are processed per
year than exist in a standing population. Market pigs live approximately
$\approx$ 6 months during which time they accumulate on the order of 5 kg per
week from feeding on corn-oil concentrates. With this relatively short residence time, there
can be a somewhat rapid turnover in the pork population. Using this lifespan, we
an compute the approximate swine standing population as 
$$
N_\text{swine}^\text{(standing pop.)} \approx \frac{1.5\cdot
10^9\,\text{swine}}{\text{year}} \cdot \frac{1}{2}\,\text{year} \approx 10^9\,\text{swine}
$${#eq:pork_standing_pop}
which is inline with the data reported by the FAO and presented in @Fig:standing_pop.

![**Sizing up global mass of consumed pork product and processed population.**
(A) Estimate for the mass of pork product produced. The daily caloric intake of
the average human is assumed to be $\approx$ 2000 kcal $\cdot$ day$^{-1}$. (B)
Estimate for the number pigs processed per year given pork product mass estimate
given in (A). Text-boxes on right-hand side of (A) and (B) correspond to the
mean and standard deviation of the reported measurements in the FAOSTAT data
base for the years 2010-2018.](figures/swine_production_estimate.pdf){#fig:pig_estimate}

### The Magnitude of Annual Livestock Processing

These estimates and comparisons with the FAO data reveal the magnitude of human
husbandry of livestock on the planet. The livestock abundances reported in
@Fig:standing_pop reveal that while humans have taken an impressive hold of the
animal biosphere, directly maintaining a population of $\approx$ 30 billion
individuals solely for the purpose of energy production. The magnitude
of these populations are presented in @Fig:livestock_numbers (A) relative to the
size of the human population. While making up only $\approx$ 6\% of the typical
Western diet, chickens outnumber humans by a factor of $\approx$ 2, being the
only single species of livestock exceeding the human population. Following
chickens are the cattle which humans outnumber by a factor of $\approx$ 5. Swine
come up last on our list of key livestock species with a swine-to-human ratio
of $\approx$ 0.1. When viewed in total, however, livestock outnumber humans by a
factor of $\approx$ 4. In the coming sections of this vignette, we will explore
in more detail the amount of crops needed to support not only the human
population, but the even larger population of livestock. 

In assessing the magnitude of human agriculture, it is worthwhile to
summarize the rate at which animals or their byproducts are consumed. In
@Fig:livestock_numbers (B), we assemble the data explored through our
previous estimates to assess the yearly flux of animals from barn to plate. A
typical omnivorous human diet mimicking that of Western populations requires
$\approx$ 10 chickens to be processed (either as poultry or via egg-laying)
per year. This is followed by swine whose lower mass yield per individual
means $\approx$ 1 pig is needed per year to sustain the pork diet of
$\approx$ 3 people. Cattle, who produce a remarkable amount of both milk and
beef per individual, are needed on the order of $\approx$ 1 cow per year
per ten people. When considered in total, the average person requires
$\approx$ 15 animals per year or $\approx$ 1200 animals per lifetime solely for food,
ignoring the number of animals needed for non-dietary requirements such as
leather, wool, and other materials.


![**Livestock by the numbers.** (A) The relative abundance of the livestock
types considered here relative to the human population. (B) The number of
animals consumed and/or processed per capita, reported in integer units.
Values provided in the number estimates correspond to the approximate
averages of the reported producing population for each product from the
FAOSTAT database for years 2010-2018. The "barn-to-table" number considers
estimate of the number of animals processed for all meat, milk, and egg
production across several animal categories as calculated by the
FAO.](figures/livestock_processing_numbers.pdf){#fig:livestock_numbers}