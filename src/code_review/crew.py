from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool

@CrewBase
class CodeReview():
	"""Code Review Crew"""

	manager_llm = LLM(
		model='ollama/qwen2.5',
		base_url='http://localhost:11434'
	)
	review_llm = LLM(
		model='ollama/mistral',
		base_url='http://localhost:11434'
	)
	write_llm = LLM(
		model='ollama/mistral',
		base_url='http://localhost:11434'
	)

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	file_read = FileReadTool(file_path='./tests/input/TaxCalculationService.java')
	file_write = FileWriterTool()

	@agent
	def clean_code_reviewer(self) -> Agent:
		return Agent(
			config=self.agents_config['clean_code_reviewer'],
			verbose=True,
			llm=self.review_llm,
			tools=[self.file_read],
		)

	@agent
	def clean_code_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['clean_code_writer'],
			verbose=True,
			llm=self.write_llm,
			tools=[self.file_read, self.file_write],
		)

	@task
	def code_review(self) -> Task:
		return Task(
			config=self.tasks_config['code_review'],
		)

	@task
	def code_write(self) -> Task:
		return Task(
			config=self.tasks_config['code_write'],
			output_file='tests/output/TaxCalculationService'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CodeReview crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.hierarchical,
			manager_llm=self.manager_llm,
			verbose=True,
		)
