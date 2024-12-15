function solution(keyinput, board) {
    let position = [0, 0];

    const xLimit = Math.floor(board[0] / 2);
    const yLimit = Math.floor(board[1] / 2);

    for (let key of keyinput) {
        switch (key) {
            case "up":
                position[1] = Math.min(position[1] + 1, yLimit); 
                break;
            case "down":
                position[1] = Math.max(position[1] - 1, -yLimit);
                break;
            case "left":
                position[0] = Math.max(position[0] - 1, -xLimit);
                break;
            case "right":
                position[0] = Math.min(position[0] + 1, xLimit);
                break;
        }
    }

    return position;
}
