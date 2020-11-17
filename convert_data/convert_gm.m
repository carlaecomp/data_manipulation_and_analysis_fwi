% Autor: Tiago Tavares
a = fopen("../data/convert/GdM_C3_400.bin");
b = fread(a, "float");

fclose(a);
nz = 283;
ny = 283;
nx = 283;
bb = reshape(b, nz,nx,ny);
X = bb(:,:,1);
imagesc(X)
figure;
cc=permute(bb, [1,3,2]);
ccc = cc(1:201,1:201,1:201);
% 
X = ccc(:,:,1);
imagesc(X)
dd=ccc(:);
d = fopen("velocity.bin",'w');
fwrite(d, dd, 'double');
fclose(d);

