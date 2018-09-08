# Python样例

一个Python代码仓库样例。
该仓库基于Django框架，实现了与软工平台OAuth接口的交互。

## 注意事项

1. Python仓库中的依赖包定义在`requirements.txt`中，使用以下命令进行安装。
   **注意**，为了支持测试数据的搜集，请确保依赖包列表中包含`coverage`以及其它用到的工具。
    ```
    pip install -r requirements.txt
    ```
2. 该仓库在Django自带的测试框架之外，使用pytest执行测试，并用coverage工具获得覆盖率。
   工具的使用方法参考`.gitlab-ci.yml`文件中的测试阶段。
   **注意**，请不要修改生成的报告的位置，以确保SonarQube能够获得测试结果。
3. `Dockerfile`的最后通过`gunicorn`以如下命令运行项目。
    ```
    gunicorn app.wsgi -b 0.0.0.0:80 --access-logfile - --log-level info
    ```
