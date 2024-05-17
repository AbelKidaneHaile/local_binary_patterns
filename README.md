# Local Binary Patterns (LBP)

In this project, I will use local binary patterns (LBP) to build a system that classifies textured images.




### It is currently being updated....


|                      | precision | recall | f1-score | support |
|----------------------|-----------|--------|----------|---------|
| KTH_aluminium_foil   | nan       | 0.00   | nan      | 216     |
| KTH_brown_bread      | 1.00      | 0.07   | 0.14     | 41      |
| KTH_corduroy         | 1.00      | 0.00   | 0.01     | 256     |
| KTH_cork             | 1.00      | 0.00   | 0.01     | 216     |
| KTH_cotton           | 1.00      | 0.16   | 0.28     | 257     |
| KTH_cracker          | 1.00      | 0.03   | 0.06     | 34      |
| KTH_linen            | 1.00      | 0.15   | 0.26     | 257     |
| KTH_orange_peel      | nan       | 0.00   | nan      | 25      |
| KTH_sponge           | 1.00      | 0.07   | 0.14     | 41      |
| KTH_styrofoam        | nan       | 0.00   | nan      | 41      |
| KTH_wool             | 1.00      | 0.02   | 0.04     | 216     |
| Kyberge_blanket1     | nan       | 0.00   | nan      | 80      |
| Kyberge_blanket2     | nan       | 0.00   | nan      | 80      |
| Kyberge_canvas1      | nan       | 0.00   | nan      | 80      |
| Kyberge_ceiling1     | 0.00      | 0.00   | nan      | 80      |
| Kyberge_ceiling2     | 0.97      | 0.72   | 0.83     | 80      |
| Kyberge_cushion1     | 0.50      | 0.01   | 0.02     | 80      |
| Kyberge_floor1       | nan       | 0.00   | nan      | 80      |
| Kyberge_floor2       | 0.00      | 0.00   | nan      | 80      |
| Kyberge_grass1       | 0.00      | 0.00   | nan      | 80      |
| Kyberge_lentils1     | nan       | 0.00   | nan      | 80      |
| Kyberge_linseeds1    | nan       | 0.00   | nan      | 80      |
| Kyberge_oatmeal1     | nan       | 0.00   | nan      | 80      |
| Kyberge_pearlsugar1  | nan       | 0.00   | nan      | 80      |
| Kyberge_rice1        | 0.00      | 0.00   | nan      | 80      |
| Kyberge_rice2        | 0.00      | 0.00   | nan      | 80      |
| Kyberge_rug1         | 0.00      | 0.00   | nan      | 80      |
| Kyberge_sand1        | nan       | 0.00   | nan      | 80      |
| Kyberge_scarf1       | nan       | 0.00   | nan      | 80      |
| Kyberge_scarf2       | 1.00      | 0.01   | 0.02     | 80      |
| Kyberge_screen1      | 0.00      | 0.00   | nan      | 80      |
| Kyberge_seat1        | 1.00      | 0.05   | 0.10     | 80      |
| Kyberge_seat2        | 0.83      | 0.06   | 0.12     | 80      |
| Kyberge_sesameseeds1 | nan       | 0.00   | nan      | 80      |
| Kyberge_stone1       | nan       | 0.00   | nan      | 80      |
| Kyberge_stone2       | nan       | 0.00   | nan      | 80      |
| Kyberge_stone3       | nan       | 0.00   | nan      | 80      |
| Kyberge_stoneslab1   | 0.00      | 0.00   | nan      | 80      |
| Kyberge_wall1        | nan       | 0.00   | nan      | 80      |
| UIUC01_bark1         | 0.00      | 0.00   | nan      | 20      |
| UIUC02_bark2         | nan       | 0.00   | nan      | 20      |
| UIUC03_bark3         | 0.00      | 0.00   | nan      | 20      |
| UIUC04_wood1         | 0.00      | 0.00   | nan      | 20      |
| UIUC05_wood2         | 0.00      | 0.00   | nan      | 20      |
| UIUC06_wood3         | 0.00      | 0.00   | nan      | 20      |
| UIUC07_water         | 0.03      | 0.30   | 0.06     | 20      |
| UIUC08_granite       | nan       | 0.00   | nan      | 20      |
| UIUC09_marble        | nan       | 0.00   | nan      | 20      |
| UIUC10_floor1        | nan       | 0.00   | nan      | 20      |
| UIUC11_floor2        | nan       | 0.00   | nan      | 20      |
| UIUC12_pebbles       | nan       | 0.00   | nan      | 20      |
| UIUC13_wall          | 0.00      | 0.00   | nan      | 20      |
| UIUC14_brick1        | 0.00      | 0.00   | nan      | 20      |
| UIUC15_brick2        | nan       | 0.00   | nan      | 20      |
| UIUC16_glass1        | nan       | 0.00   | nan      | 20      |
| UIUC17_glass2        | nan       | 0.00   | nan      | 20      |
| UIUC18_carpet1       | nan       | 0.00   | nan      | 20      |
| UIUC19_carpet2       | nan       | 0.00   | nan      | 20      |
| UIUC20_upholstery    | 0.00      | 0.00   | nan      | 20      |
| UIUC21_wallpaper     | nan       | 0.00   | nan      | 20      |
| UIUC22_fur           | 0.00      | 0.00   | nan      | 20      |
| UIUC23_knit          | 0.00      | 0.00   | nan      | 20      |
| UIUC24_corduroy      | 0.00      | 0.60   | 0.01     | 20      |
| UIUC25_plaid         | 0.00      | 0.00   | nan      | 20      |
| accuracy             |           |        | 0.04     | 4340    |
| macro avg            | 0.36      | 0.04   | 0.14     | 4340    |
| weighted avg         | 0.64      | 0.04   | 0.14     | 4340    |
