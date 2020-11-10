% Autor: Tiago Tavares
a = fopen("../data/view/dobs_v401.bin");
b = fread(a, "double");
fclose(a);

dx = 25;
dy = 25;
dt = 0.001;

sxi=40;
syi=40;
dsx=40;
dsy=40;
nsrc=16;
gxi = 0;
gyi = 0;
gxf = 201;
gyf = 201;
dgx= 2;
dgy= 2;
nx = floor((gxf-gxi)/2)+1;
ny = floor((gxf-gxi)/2)+1;

nt = 401;

x = 0:dx:(nx-1)*dx;
y = 0:dy:(ny-1)*dy;
% t = 0:dt:(nt-1)*dt;
t = 0:(nt-1);

shot_i=3;
shot_f=4;
b = b(shot_i*nx*ny*nt:shot_f*nx*ny*nt-1);
bb = reshape(b, nt,ny,nx);

for ii=1:5
    bplot = bb(:,:,ii);
    imagesc(bplot); colorbar; colormap gray;
    pause(0.1)
    figure;
end
