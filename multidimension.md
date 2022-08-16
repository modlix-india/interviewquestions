# Problem : Developer Strange in the Multidimension of Madness

### Array Dimensions and axes:

1 Dimension Array :

```
[1,2,3,4,5]

has only one axis
```

2 Dimension Array :

```
[[1,2,3], [4,5,6]]

has two axes 0 and 1. Where 0 is x axis and 1 is y axis. To get '5' you need to access axis 1 and then 0 means array[1][2] here axis 1 value is 1 and axis 0 value is 2
```

3 Dimension Array :

```
[[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]

has three axes 0, 1 and 2. Where 0 is x axis, 1 is y axis and 2 is z axis. To get '9' you need to axis 2 and then 1 and then 0 means array[1][0][2].
```

4 Dimension Array :

```
[[[[1,2,3], [3,4,5]], [[1,2,3], [3,4,5]]], [[[1,2,3], [3,4,5]], [[1,2,3], [3,4,5]]]]

has four axes 0,1,2 and 3.
```

N Dimension Array :

```
[[[[[[...]]]]], [[[[[...]]]]] ...]

has n axes 0,1,2,3,...n. To access one scalar element you need to get to n th axis first and (n-1) th and so on and in the end you will access 0th axis.

```

### Problem :

Write a function or class to transpose a given N-Dimension Array. Please use your own assumptions to define an N-Dimension array data strucutre.

1. When an 1D array is given, the function should throw an exception or an error as you cannot transpose an 1D array.

2. When any other dimension array other than 1D is given, it should take another argument of array of integers how the axes have to be arranged.

### Examples:

1.

```
a = [[1,2],[3,4]];
transpose(a, [1, 0]);
display(a);
```

```
[[1 3]
 [2 4]]
```

In this case it works like a matrix transpose operation.

2.

```
a = [[1,2],[3,4]];
transpose(a, [0, 1]);
display(a);
```

```
[[1 2]
 [3 4]]
```

In this case no transpose will have to be done as 0th axes remain in 0th index, 1st axes remain in 1st index.

3.

```
a = [[[1,2,3],[3,4,5]],[[1,2,3],[3,4,5]]];
transpose(a, [2, 0, 1]);
display(a);
```

```
[
  [
    [1 3]
    [1 3]
  ]

  [
    [2 4]
    [2 4]
  ]

  [
    [3 5]
    [3 5]
  ]
]
```

In this case of 2x2x3 we are transposing the last axes to first making it return 3x2x2. Meaning two 2x3 matrices are trasposed to three 2x2 matrices.
