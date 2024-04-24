function grid = gen_treats(grid)
    % generates treats at each corner of traversable area, using 4
    [rows, cols] = size(grid);
    
    % generate the treats in the four corners of the map
    treat_pos = {[2, 2], [2, cols-1], [rows-1, 2], [rows-1, cols-1]};
    for i = 1:numel(treat_pos)
        grid(treat_pos{i}(1), treat_pos{i}(2)) = int8(4);
    end
end

