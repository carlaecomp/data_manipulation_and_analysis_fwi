% Autor: Tiago Tavares
%%
zi=4; %gz
space=2; %dgx
space_s = 40; %dsx
g0=0; %gxi
gf=201; % gxf

dh=25; %dx dy dz
dt=0.001;
f=5; %fpeak
bw = 30;

xp=40; %sxi 
yp=40; %syi
zp=35;
% xs=11; ys=11; zs=6;

%%

zsi=0; %sz

nxs=length(1:space_s:gf);
nys=length(1:space_s:gf);
xs = [];
ys = [];

nsrc = 169; %n_src
if nsrc >= nxs*nys
    nsrc=nxs*nys;
end

src_i = 0;
for xi=0:nxs-1
    for yi=0:nys-1
        ind = xi*nys + yi;
        xs(ind+1) = space_s*xi;
        ys(ind+1) = space_s*yi;
        src_i=src_i+1;
        if src_i>=nsrc
           break 
        end
    end
    if src_i>=nsrc
       break 
    end
end
zs = zsi*ones(nsrc,1)';

%%

nx=length(1:space:gf);
ny=length(1:space:gf);
nrcv = nx*ny;

xr = zeros(nrcv,1);
yr = zeros(nrcv,1);
zr = zi*ones(nrcv,1);

for xi=0:nx-1
    for yi=0:ny-1
        ind = xi*ny + yi;
        xr(ind+1) = space*xi;
        yr(ind+1) = space*yi;
    end
end

close all
figure1 = figure;
axes1 = axes('Parent',figure1);
plot3(xs*dh, ys*dh, zs*dh, 'bd', 'LineWidth', 2); 
hold on;
% plot3(11, 11, 31, 'r+', 'LineWidth', 2);
plot3(xr*dh, yr*dh, zr*dh, 'r+', 'LineWidth', 2);
% plot3(xp*dh, yp*dh, zp*dh, 'ko', 'LineWidth', 2);
grid on;
axis([g0 gf g0 gf g0 gf]*dh)
legend('sources', 'receivers');
% legend('source', 'receivers', 'perturbation');
zlabel('z [m]'); ylabel('y [m]'); xlabel('x [m]');
view(axes1,[-46.7527918781726 2.11121495327104]);
set(gca,'FontName','Arial','FontSize',13);
% view(axes1,[-73.8502538071067 15.0939252336449]);

