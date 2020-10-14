import turtle as t


def draw_tree1(branch):
    # 条件满足先画右边
    if branch > 10:
        # 绘制最开始的树干
        t.fd(branch)
        # 然后右转30，第一个右分支
        t.right(30)
        # 继续画右边的,走不动了往左边转60和下面一样用到了递归
        draw_tree1(branch / 1.5)
        # 然后左转60  进入向左绘制
        t.left(60)
        # 继续画左边的，走不动了右转30回到最后一步的之前那个节点
        draw_tree1(branch / 1.5)
        t.right(30)
        # 给最后二个树枝画上雪白的叶子
        # 这个条件可以根据实际设置
        if branch / 1.5 <= 10:
            t.pencolor("snow")
        else:
            # 褐色
            t.pencolor("Tan")
        # 当递归条件不满足的时候，后退一个节点
        t.backward(branch)  


if __name__ == '__main__':
    #  枝条总数
    my_branch = 60

    draw_tree1(my_branch)
