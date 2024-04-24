function grid = gen_paths(grid)
    % works only for treat position in top left of matrix
    treat_pos = {[2, 2]}; % treat position assuming grid size >= 5x10

    for i = 1:numel(treat_pos)
        start = treat_pos{i};
        get_to = locate_mid(grid);

        go = true;
        while go
            choice = randi([1, 2]); % 1 for down, 2 for right
            if choice == 1
                if start(1) < get_to(1)
                    start(1) = start(1) + 1;
                    if ~isequal(start, get_to)
                        grid(start(1), start(2)) = int8(9);
                    end
                end
            elseif choice == 2
                if start(2) < get_to(2)
                    start(2) = start(2) + 1;
                    if ~isequal(start, get_to)
                        grid(start(1), start(2)) = int8(9);
                    end
                end
            end

            if isequal(start, get_to)
                go = false;
            end
        end
    end
end

function mid = locate_mid(grid)
    [rows, cols] = size(grid);
    mid = [floor(rows/2), floor(cols/2)];
end
