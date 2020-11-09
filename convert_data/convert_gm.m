% Autor: Tiago Tavares
a = fopen("GdM_C3_fwi.bin");
b = fread(a, "float");

fclose(a);
nz = 283;
ny = 910;
nx = 758;
bb = reshape(b, nz,nx,ny);
bb = bb(1:201,1:201,1:201);
imagesc(bb(:,:,1))
figure
surf(bb(:,:,1))
% cc=permute(bb, [1,3,2]);
% ccc = cc(1:201,1:201,1:201);
% 
% dd=ccc(:);
% d = fopen("velocity.bin",'w');
% fwrite(d, dd, 'double');
% fclose(d);

