import imageio
def create_gif(image_list, gif_name, durations):
    name = []
    # 把图片加进列表
    for i in image_list:
        name.append(imageio.imread(i))
    # 保存为gif图
    imageio.mimsave(gif_name, name, 'GIF', duration=durations)

def main():
    image_list = ['1.png', '2.png', '3.png']
    gif_name = "new.gif"
    duration = 1
    create_gif(image_list, gif_name, duration)

if __name__ == '__main__':
    main()

