fp   = fopen('../to_mamute_form/data/velocity_model.bin');
velocity_model = fread(fp,'float');
fclose(fp);
A = reshape(velocity_model,201,201,201);
imagesc(A(:,:,1))
figure;
surf(A(:,:,1))
figure