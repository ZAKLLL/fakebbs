#!/bin/bash


while true; do

    
    # 检查 git pull 是否有更新
    if git pull | grep -q 'Already up to date.'; then
        echo "No changes detected. Skipping restart."
            # 检查应用是否正在运行
        if ! pgrep -f "uvicorn main:app" > /dev/null; then
            echo "Application is not running. Starting it now..."
            nohup uvicorn main:app --host 0.0.0.0 --port 80 --reload >>log.log 2>&1 &
            echo "Application started!"
        else
            echo "Application is already running."
        fi
    else
        echo "Changes detected. Proceeding with restart."
        
        # 找到并停止当前运行的进程
        PID=$(pgrep -f "uvicorn main:app")
        if [ ! -z "$PID" ]; then
            echo "Stopping current process (PID: $PID)..."
            kill $PID
            sleep 2  # 给进程一些时间来完全停止
        fi

        # 启动新的应用程序实例
        echo "Starting new instance of the application..."
        nohup uvicorn main:app --host 0.0.0.0 --port 80 --reload  >>log.log 2>&1 &
        echo "Reload complete!"
    fi



    # 等待2分钟
    sleep 120
done