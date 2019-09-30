def init_params(model):
    for p in model.parameters():
        if (p.dim() > 1):
            nn.init.xavier_normal_(p)
        else:
            nn.init.uniform_(p, 0.1, 0.2)


init_params(G)
init_params(D)

optimizer_g = optim.Adam(G.parameters(), lr=0.0002)
optimizer_d = optim.Adam(D.parameters(), lr=0.0002)

p_real_trace = []
p_fake_trace = []

for epoch in range(200):

    run_epoch(G, D, optimizer_g, optimizer_d)
    p_real, p_fake = evaluate_model(G, D)

    p_real_trace.append(p_real)
    p_fake_trace.append(p_fake)

    if ((epoch + 1) % 50 == 0):
        print('(epoch %i/200) p_real: %f, p_g: %f' % (epoch + 1, p_real, p_fake))
        imshow_grid(G(sample_z(16)).view(-1, 1, 28, 28))