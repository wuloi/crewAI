from crewai import Agent, Crew, Task, LLM

# 创建研究团队
researcher = Agent(
    role="市场分析师",
    goal="收集行业数据",
    backstory="资深数据分析专家",
    llm = LLM(
        model="ollama/llama3.2:latest",
        base_url="http://localhost:11434"
    ),
    verbose=True,
)

writer = Agent(
    role="内容创作",
    goal="生成分析报告",
    backstory="专业文案作家",
    verbose=True,
    llm = LLM(
        model="ollama/llama3.2:latest",
        base_url="http://localhost:11434"
    )
)

# 定义协同任务
research_task = Task(
    description="收集2023年AI行业趋势数据",
    expected_output="结构化数据表格",
    agent=researcher
)

writing_task = Task(
    description="生成年度趋势报告",
    expected_output="Markdown格式的10页分析报告",
    agent=writer,
    context=[research_task]
)

# 创建执行团队
team = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True,
)

if __name__ == "__main__":
    result = team.kickoff()
    print("\n执行结果:")
    print(result)