// Gmsh project created on Mon Feb 19 22:33:33 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {50, 0, 0, 1.0};
//+
Point(3) = {10, 45, 0, 1.0};
//+
Point(4) = {10, 60, 0, 1.0};
//+
Point(5) = {0, 60, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {5, 1};
//+
Curve Loop(1) = {1, 2, 3, 4, 5};
//+
Plane Surface(1) = {1};
//+
Physical Curve("fixed", 6) = {1};
//+
Physical Curve("load", 7) = {5};
//+
Physical Surface("dom", 8) = {1};

Transfinite Curve{:} = 3;//+
Recombine Surface {1};
