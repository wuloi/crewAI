from crewai import Agent, Crew, Task, LLM

# 创建管理型智能体
manager = Agent(
    role="项目总监",
    goal="优化任务分配",
    backstory="资深项目管理专家",
    llm = LLM(
        model="ollama/llama3.2:latest",
        base_url="http://localhost:11434"
    ),
    verbose=True,
)

# 动态任务生成函数
def dynamic_task_creation(market_condition):
    if market_condition == "volatile":
        return Task(
            description="执行风险评估",
            expected_output="包含风险指标和应对策略的评估报告",
            agent=manager
        )
    else:
        return Task(
            description="推进市场扩展",
            expected_output="包含扩展策略和执行计划的方案文档",
            agent=manager
        )

if __name__ == "__main__":
    # 模拟市场条件（可修改为实际输入）
    market_status = "volatile"
    
    # 创建动态任务
    selected_task = dynamic_task_creation(market_status)
    
    # 组建执行团队
    team = Crew(
        agents=[manager],
        tasks=[selected_task],
        verbose=True,
    )
    
    # 执行任务
    print(f"\n当前市场状态: {market_status}")
    result = team.kickoff()
    print("\n执行结果:")
    print(result)