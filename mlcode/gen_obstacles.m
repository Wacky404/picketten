function grid = gen_obstacles(grid)
    % randomly generates obstacles, using 1
    [rows, cols] = size(grid);

    for i = 2:rows-1
        for j = 2:cols-1
            grid(i,j) = int8(randi([0, 1]));
        end
    end
end
