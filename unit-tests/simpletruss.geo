// Gmsh project created on Tue Jan 23 10:01:38 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0.0, 0.0, 0.0, 1.0};
//+
Point(2) = {2.0, 0.0, 0.0, 1.0};
//+
Point(3) = {2.0, 2.0, 0.0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 1};
//+
Physical Curve("truss", 4) = {1, 2, 3};
//+
Physical Point("fixed", 5) = {1};
//+
Physical Point("fixedy", 6) = {2};
//+
Physical Point("force1", 7) = {3};

Transfinite Curve{:} = 1;