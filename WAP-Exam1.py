import Queue

def copy(ground):
  return [ [y for y in x] for x in ground]

def bfs(x,y,ground,rows,cols):

  if ground[x][y] == -1:
    return -1
  else:
    max_score = -1
    queue = Queue.Queue()
    queue.put(( (x,y), ground, int(ground[x][y]) ))
    ground[x][y] = -1
    while(queue.empty() == False):
      (now_x, now_y), now_map, now_score = queue.get()
      for move_x, move_y in [(1,0), (0,1), (-1,0)]:
        new_x, new_y = ((now_x + move_x) % cols), ((now_y + move_y) % rows)
        if now_map[new_x][new_y] != -1:
          new_map = copy(now_map)
          new_map[new_x][new_y] = -1
          new_score = ((now_score + now_map[new_x][new_y]) 
                                   if (new_x == (now_x + move_x) and new_y == (now_y + move_y))
                                   else now_map[new_x][new_y])
          if new_score > max_score:
            max_score = new_score
          queue.put(((new_x,new_y), new_map, new_score ))
    return max_score


if __name__ == '__main__':
  rows, cols = map(int, raw_input().split())
  ground = [map(int, raw_input().split()) for x in range(rows)]
  print max( bfs(y, 0, copy(ground),rows,cols) for y in range(rows))
  # bfs(1, 0, copy(ground),rows,cols)


