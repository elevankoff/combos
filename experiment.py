import subprocess
import click

@click.command()
@click.option('--experiments-count', default=5)
def experiment(experiments_count):
    subprocess.check_call(['./generator'])
    experiments_sum = 0
    for i in range(0, experiments_count):
        execute = subprocess.Popen(['./execute'], stdout=subprocess.PIPE)
        results = subprocess.check_output(['grep', 'Results valid'], stdin=execute.stdout)
        execute.wait()

        project_results = results.decode('UTF-8').split('\n')
        results = []
        for project_result in project_results:
            if not project_result:
                continue
            valid_results_str = project_result[19:project_result.find('(')-1].replace(',', '')
            valid_results = int(valid_results_str)
            results.append(valid_results)
            results_str = [str(x) for x in results]
        projects_sum = sum(results)
        experiments_sum += projects_sum
        print(f"{'+'.join(results_str)}={projects_sum}")
    print(f"Sum of valid results of {experiments_count} experiments: {experiments_sum}")
    


if __name__ == '__main__':
    experiment()
