from downloader.universal import download_video


def main():
    bv_number = "BV17fw6ekE4h"
    url = f"https://www.bilibili.com/video/{bv_number}"
    video_path = download_video(url)


if __name__ == '__main__':
    main()
