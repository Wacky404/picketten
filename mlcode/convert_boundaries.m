function grid = convert_boundaries(grid)
    % converts boundaries of grid to walls, in this case 1
    [rows, cols] = size(grid);

    % Convert top and bottom rows to walls
    grid(1,:) = int8(1);
    grid(rows,:) = int8(1);

    % Convert left and right columns to walls
    grid(:,1) = int8(1);
    grid(:,cols) = int8(1);
end
