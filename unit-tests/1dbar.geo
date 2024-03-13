// Gmsh project created on Thu Feb 15 14:37:26 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {3, 0, 0, 1.0};
//+
Point(3) = {4, 0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Physical Point("fixed", 3) = {1, 3};
//+
Physical Curve("bar", 4) = {1, 2};
//+
Physical Point("force", 5) = {2};

Transfinite Curve{:} = 1;