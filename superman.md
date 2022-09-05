# Problem: Superman and Bottle City of Kandor

Superman wants to restore the Bottle city of Kandor on a planet revolving around a Red star similar to Rao, the star Krypton was spinning around.

## Task:

You must write a function or method to find the suitable planet around an appropriate red star. To do so, you need to find the energy output that a world receives from the home star/stars. In some solar systems, there can be more than one star. The energy a planet gets is computed by adding the output received from each star in the system. The energy a world gets from one star is calculated by multiplying the star's energy output with the inverse of the distance.

## Input:

One of the inputs is a three-dimensional array.

```
[
	[
        [
		    0.433, // Stars output
		    200 // Distance from the star
	    ]
    ], // Solar System with one star
	[
        [
            0.89, // Star one's output
            400 // Distance from the star one
        ],
        [
            0.6, // Star two's output
            300 // Distance from the star two
        ]
    ], // Solar System with two stars
] // Two solar systems
```

The other input is the array of range suitable for the people of kandor to live

## Example:

findPlanet([[[0.433, 200]], [[0.89, 400], [0.6, 300]]], [0.003, 0.005]);

returns 1;

## Explanation:

First system outputs 0.002165
Second system first star outputs 0.002225, and second start outputs 0.002 so total output the planet gets is 0.004225. Since second system is within the range 0.003 and 0.005 it returns 1
