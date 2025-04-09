#!/bin/bash

export CREWAI_TELEMETRY=false
echo '=== 运行基础任务编排示例 ==='
python3 demo/basic_crew.py

echo '=== 运行动态任务分配示例 ==='
python3 demo/dynamic_tasks.py