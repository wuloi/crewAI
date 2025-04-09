from crewai import Agent, Crew, Task, LLM
from crewai_tools import (
    CodeInterpreterTool,
    DataAnalysisTool,
    LegalReviewTool,
    BudgetAnalysisTool,
    RecruitmentAutomationTool
)

# 定义公司核心智能体
ceo = Agent(
    role="首席执行官",
    goal="制定公司战略方向",
    backstory="拥有20年管理经验的行业领袖",
    tools=[],
    verbose=True,
    llm=LLM(
        model="ollama/llama3.2:latest",
        base_url="http://localhost:11434"
    )
)

rd_agent = Agent(
    role="研发总监",
    goal="领导产品技术研发",
    backstory="拥有10项专利的技术专家",
    tools=[CodeInterpreterTool()],
    verbose=True
)

marketing_agent = Agent(
    role="市场总监",
    goal="制定市场推广策略",
    backstory="成功打造多个爆款产品的营销专家",
    tools=[DataAnalysisTool()],
    verbose=True
)

hr_agent = Agent(
    role="人力资源总监",
    goal="优化人才结构",
    backstory="精通组织行为学的HR专家",
    tools=[RecruitmentAutomationTool()],
    verbose=True
)

finance_agent = Agent(
    role="财务总监",
    goal="控制财务风险",
    backstory="CPA持证的风险控制专家",
    tools=[BudgetAnalysisTool()],
    verbose=True
)

legal_agent = Agent(
    role="法务总监",
    goal="确保合规运营",
    backstory="处理过数百起商业诉讼的资深律师",
    tools=[LegalReviewTool()],
    verbose=True
)

# 定义年度战略任务
strategy_task = Task(
    description="制定2024年度公司战略",
    expected_output="包含市场定位、研发方向、财务目标的战略文档",
    agent=ceo,
    context=[],
    output_file="annual_strategy.md"
)

# 产品研发流程任务
product_task = Task(
    description="开发新一代智能客服系统",
    expected_output="包含技术方案、市场计划、法律风险评估的完整项目文档",
    agent=rd_agent,
    context=[strategy_task],
    collaborators=[marketing_agent, legal_agent],
    output_file="product_roadmap.pdf"
)

# 人才招聘任务
recruitment_task = Task(
    description="执行季度人才扩充计划",
    expected_output="包含岗位需求、薪资结构和法律合规的招聘方案",
    agent=hr_agent,
    context=[strategy_task],
    collaborators=[finance_agent, legal_agent],
    output_file="recruitment_plan.docx"
)

# 创建公司执行团队
corporate_crew = Crew(
    agents=[ceo, rd_agent, marketing_agent, hr_agent, finance_agent, legal_agent],
    tasks=[strategy_task, product_task, recruitment_task],
    verbose=2,
    process="hierarchical"
)

if __name__ == "__main__":
    result = corporate_crew.kickoff()
    print("\n战略执行结果:")
    print(result)