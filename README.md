# Visualisation-of-definite-integral-to-calculate-area-under-curve

The area under a curve between two points can be found by doing a definite
integral between the two points. To find the area under the curve y = f(x) between x = a and
x = b, integrate y = f(x) between the limits of a and b. This application of definite integrals
can be broadly used to calculate the amount of water flowing in a river working on a similar
pattern as a water flow meter. We can note the depth and velocity at the points in the river
and feed the data into a program to calculate the flow and generate a graph of the cross-
section of the river with the data on it. We can demonstrate how taking the Riemann Sum
for the graph would give the amount of flow more accurately than taking an average or
weighted average of the velocity.
Consider the velocity and depth of the river to be v L , d L and v R , d R on left and right side
respectively. For a point x (x L &lt;x&lt;_x R ), we can approximate the velocity and depth using linear
interpolation as:

<img width="404" alt="image" src="https://user-images.githubusercontent.com/78687612/184166908-2d3f77fe-771a-45ca-9ecb-e437b7907c83.png">


To take the Riemann Sum, we will take the depth at each point and multiply by the velocity
at that point and the width of the interval. Therefore, the flow of the section is given by:

<img width="200" alt="image" src="https://user-images.githubusercontent.com/78687612/184166988-40f9abdf-d455-4110-ae84-80f31050e76b.png">


Also, we will compute the difference produced by following the approaches of average,
weighted average and Riemann Sum.

Outputs : 

<img width="339" alt="image" src="https://user-images.githubusercontent.com/78687612/184167588-0772eec6-ae96-4aaf-8541-e08f5dd7a48d.png">
<img width="392" alt="image" src="https://user-images.githubusercontent.com/78687612/184167706-09314c99-c432-4ffb-88b9-339a87d9f6df.png">
<img width="833" alt="image" src="https://user-images.githubusercontent.com/78687612/184167814-288293d1-0f0e-4842-b155-0e0caba4e29a.png">
