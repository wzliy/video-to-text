import subprocess
from pathlib import Path
from typing import Optional
from ..utils.logger import logger


def download_video(
        url: str,
        output_dir: str = "./outputs/videos",
        proxy: Optional[str] = None
) -> str:
    """
        使用you-get下载视频
        Args:
            url: 视频URL（支持B站/YouTube/优酷等）
            output_dir: 视频存储目录
            proxy: 代理设置（示例：'http://127.0.0.1:1080'）
        Returns:
            下载视频的完整路径
    """
    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        cmd = [
            "you-get",
            "--output-dir", output_dir,
            "--no-caption", # 不下载字幕
            url
        ]

        if proxy:
            cmd.extend(["--http-proxy", proxy])

        # 执行下载命令
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # 解析下载路径（从输出日志中提取）
        downloaded_file = None
        for line in result.stdout.split('\n'):
            if "Downloading" in line and "..." in line:
                downloaded_file = line.split("...")[1].strip()
                break

        if downloaded_file:
            video_path = str(Path(output_dir) / downloaded_file)
            logger.success(f"视频已下载至：{video_path}")
            return video_path
        else:
            raise ValueError("无法解析下载文件名")

    except subprocess.CalledProcessError as e:
        logger.error(f"下载失败：{e.output}")
        raise


