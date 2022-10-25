function out = goldenSection(func, l, u)
    phi = (sqrt(5) - 1) / 2;
    while true
        x1 = u - (u-l) * phi;
        x2 = l + (u-l) * phi;
        if abs((x1 - x2) / x1) < 10^-6
            out = (x1 + x2) / 2;
            return
        end
        if func(x1) > func(x2)
            u = x2;
        else
            l = x1;
        end
    end
end
