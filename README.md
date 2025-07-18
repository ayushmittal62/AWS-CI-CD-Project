# End-to-End ML: Student Performance Prediction

An end-to-end machine learning project for predicting student performance — from data preparation, model training, pipeline orchestration to Dockerization and AWS deployment.

---

## 🔍 Features

- **Data ingestion & preprocessing**  
  Load CSV data, perform cleaning, handle missing values, encode categorical features, and scale numeric variables.

- **Exploratory Data Analysis (EDA)**  
  Visualize patterns and relationships in the dataset.

- **Model training & evaluation**  
  Train ML models, evaluate using metrics, and save the trained pipeline.

- **ML pipeline**  
  Modularized pipeline using Python scripts for better maintainability.

- **Model logging & tracking**  
  Integrated MLflow (or similar) for tracking experiments.

- **Packaging & serving**  
  Flask API exposing endpoints for predictions via HTML forms and JSON.

- **Containerization**  
  Dockerfile for building a containerized ML inference service.

- **CI/CD with GitHub Actions**  
  Automate Docker image building and deployment to AWS EC2 using self-hosted runner.

- **AWS Deployment**  
  Deployed using ECR + EC2, with GitHub Actions and IAM integration.

---

## 🛠️ Project Setup

```bash
git clone https://github.com/ayushmittal62/End-to-End-ML.git
cd End-to-End-ML
pip install -r requirements.txt

```
End To ENd Ml
├─ .ebextensions
│  └─ python.config
├─ application.py
├─ artifacts
│  ├─ data.csv
│  ├─ model.pkl
│  ├─ preprocessor.pkl
│  ├─ test.csv
│  └─ train.csv
├─ catboost_info
│  ├─ catboost_training.json
│  ├─ learn
│  │  └─ events.out.tfevents
│  ├─ learn_error.tsv
│  ├─ time_left.tsv
│  └─ tmp
├─ logs
│  ├─ 07_12_2025_12_53_14.log
│  ├─ 07_12_2025_13_07_50.log
│  ├─ 07_15_2025_16_47_17.log
│  ├─ 07_16_2025_14_09_25.log
│  ├─ 07_16_2025_14_10_46.log
│  ├─ 07_16_2025_14_17_18.log
│  ├─ 07_16_2025_14_22_38.log
│  ├─ 07_17_2025_13_23_04.log
│  ├─ 07_17_2025_13_23_57.log
│  ├─ 07_17_2025_13_24_18.log
│  ├─ 07_17_2025_13_27_13.log
│  ├─ 07_17_2025_13_28_29.log
│  ├─ 07_17_2025_14_12_21.log
│  ├─ 07_17_2025_14_12_23.log
│  ├─ 07_17_2025_14_14_17.log
│  ├─ 07_17_2025_14_15_18.log
│  ├─ 07_17_2025_14_19_33.log
│  └─ 07_17_2025_14_19_35.log
├─ notebook
│  └─ data
│     ├─ catboost_info
│     │  ├─ catboost_training.json
│     │  ├─ learn
│     │  │  └─ events.out.tfevents
│     │  ├─ learn_error.tsv
│     │  ├─ time_left.tsv
│     │  └─ tmp
│     ├─ EDA.ipynb
│     ├─ model_training.ipynb
│     └─ stud.csv
├─ README.md
├─ requirements.txt
├─ setup.py
├─ src
│  ├─ components
│  │  ├─ data_ingestion.py
│  │  ├─ data_transformation.py
│  │  ├─ model_trainer.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ data_ingestion.cpython-38.pyc
│  │     ├─ data_transformation.cpython-38.pyc
│  │     ├─ model_trainer.cpython-38.pyc
│  │     └─ __init__.cpython-38.pyc
│  ├─ exception.py
│  ├─ logger.py
│  ├─ pipeline
│  │  ├─ predict_pipeline.py
│  │  ├─ train_pipeline.py
│  │  └─ __pycache__
│  │     └─ predict_pipeline.cpython-38.pyc
│  ├─ utils.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ exception.cpython-38.pyc
│     ├─ logger.cpython-38.pyc
│     ├─ utils.cpython-38.pyc
│     └─ __init__.cpython-38.pyc
├─ templates
│  ├─ home.html
│  └─ index.html
└─ venv
   ├─ Include
   ├─ Lib
   │  └─ site-packages
   │     ├─ easy_install.py
   │     ├─ pip
   │     │  ├─ _internal
   │     │  │  ├─ build_env.py
   │     │  │  ├─ cache.py
   │     │  │  ├─ cli
   │     │  │  │  ├─ autocompletion.py
   │     │  │  │  ├─ base_command.py
   │     │  │  │  ├─ cmdoptions.py
   │     │  │  │  ├─ command_context.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ main_parser.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ progress_bars.py
   │     │  │  │  ├─ req_command.py
   │     │  │  │  ├─ spinners.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ autocompletion.cpython-38.pyc
   │     │  │  │     ├─ base_command.cpython-38.pyc
   │     │  │  │     ├─ cmdoptions.cpython-38.pyc
   │     │  │  │     ├─ command_context.cpython-38.pyc
   │     │  │  │     ├─ main.cpython-38.pyc
   │     │  │  │     ├─ main_parser.cpython-38.pyc
   │     │  │  │     ├─ parser.cpython-38.pyc
   │     │  │  │     ├─ progress_bars.cpython-38.pyc
   │     │  │  │     ├─ req_command.cpython-38.pyc
   │     │  │  │     ├─ spinners.cpython-38.pyc
   │     │  │  │     ├─ status_codes.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ commands
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ completion.py
   │     │  │  │  ├─ configuration.py
   │     │  │  │  ├─ debug.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ hash.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ list.py
   │     │  │  │  ├─ search.py
   │     │  │  │  ├─ show.py
   │     │  │  │  ├─ uninstall.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ cache.cpython-38.pyc
   │     │  │  │     ├─ check.cpython-38.pyc
   │     │  │  │     ├─ completion.cpython-38.pyc
   │     │  │  │     ├─ configuration.cpython-38.pyc
   │     │  │  │     ├─ debug.cpython-38.pyc
   │     │  │  │     ├─ download.cpython-38.pyc
   │     │  │  │     ├─ freeze.cpython-38.pyc
   │     │  │  │     ├─ hash.cpython-38.pyc
   │     │  │  │     ├─ help.cpython-38.pyc
   │     │  │  │     ├─ install.cpython-38.pyc
   │     │  │  │     ├─ list.cpython-38.pyc
   │     │  │  │     ├─ search.cpython-38.pyc
   │     │  │  │     ├─ show.cpython-38.pyc
   │     │  │  │     ├─ uninstall.cpython-38.pyc
   │     │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ configuration.py
   │     │  │  ├─ distributions
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ installed.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │     ├─ installed.cpython-38.pyc
   │     │  │  │     ├─ sdist.cpython-38.pyc
   │     │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ index
   │     │  │  │  ├─ collector.py
   │     │  │  │  ├─ package_finder.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ collector.cpython-38.pyc
   │     │  │  │     ├─ package_finder.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ locations.py
   │     │  │  ├─ main.py
   │     │  │  ├─ models
   │     │  │  │  ├─ candidate.py
   │     │  │  │  ├─ direct_url.py
   │     │  │  │  ├─ format_control.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ link.py
   │     │  │  │  ├─ scheme.py
   │     │  │  │  ├─ search_scope.py
   │     │  │  │  ├─ selection_prefs.py
   │     │  │  │  ├─ target_python.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ candidate.cpython-38.pyc
   │     │  │  │     ├─ direct_url.cpython-38.pyc
   │     │  │  │     ├─ format_control.cpython-38.pyc
   │     │  │  │     ├─ index.cpython-38.pyc
   │     │  │  │     ├─ link.cpython-38.pyc
   │     │  │  │     ├─ scheme.cpython-38.pyc
   │     │  │  │     ├─ search_scope.cpython-38.pyc
   │     │  │  │     ├─ selection_prefs.cpython-38.pyc
   │     │  │  │     ├─ target_python.cpython-38.pyc
   │     │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ network
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ lazy_wheel.py
   │     │  │  │  ├─ session.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ xmlrpc.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ auth.cpython-38.pyc
   │     │  │  │     ├─ cache.cpython-38.pyc
   │     │  │  │     ├─ download.cpython-38.pyc
   │     │  │  │     ├─ lazy_wheel.cpython-38.pyc
   │     │  │  │     ├─ session.cpython-38.pyc
   │     │  │  │     ├─ utils.cpython-38.pyc
   │     │  │  │     ├─ xmlrpc.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ operations
   │     │  │  │  ├─ build
   │     │  │  │  │  ├─ metadata.py
   │     │  │  │  │  ├─ metadata_legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  ├─ wheel_legacy.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ metadata.cpython-38.pyc
   │     │  │  │  │     ├─ metadata_legacy.cpython-38.pyc
   │     │  │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │  │     ├─ wheel_legacy.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ install
   │     │  │  │  │  ├─ editable_legacy.py
   │     │  │  │  │  ├─ legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ editable_legacy.cpython-38.pyc
   │     │  │  │  │     ├─ legacy.cpython-38.pyc
   │     │  │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ prepare.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ check.cpython-38.pyc
   │     │  │  │     ├─ freeze.cpython-38.pyc
   │     │  │  │     ├─ prepare.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pyproject.py
   │     │  │  ├─ req
   │     │  │  │  ├─ constructors.py
   │     │  │  │  ├─ req_file.py
   │     │  │  │  ├─ req_install.py
   │     │  │  │  ├─ req_set.py
   │     │  │  │  ├─ req_tracker.py
   │     │  │  │  ├─ req_uninstall.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ constructors.cpython-38.pyc
   │     │  │  │     ├─ req_file.cpython-38.pyc
   │     │  │  │     ├─ req_install.cpython-38.pyc
   │     │  │  │     ├─ req_set.cpython-38.pyc
   │     │  │  │     ├─ req_tracker.cpython-38.pyc
   │     │  │  │     ├─ req_uninstall.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ resolution
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ legacy
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ resolver.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ resolvelib
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ candidates.py
   │     │  │  │  │  ├─ factory.py
   │     │  │  │  │  ├─ provider.py
   │     │  │  │  │  ├─ requirements.py
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │  │     ├─ candidates.cpython-38.pyc
   │     │  │  │  │     ├─ factory.cpython-38.pyc
   │     │  │  │  │     ├─ provider.cpython-38.pyc
   │     │  │  │  │     ├─ requirements.cpython-38.pyc
   │     │  │  │  │     ├─ resolver.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ self_outdated_check.py
   │     │  │  ├─ utils
   │     │  │  │  ├─ appdirs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ compatibility_tags.py
   │     │  │  │  ├─ datetime.py
   │     │  │  │  ├─ deprecation.py
   │     │  │  │  ├─ direct_url_helpers.py
   │     │  │  │  ├─ distutils_args.py
   │     │  │  │  ├─ encoding.py
   │     │  │  │  ├─ entrypoints.py
   │     │  │  │  ├─ filesystem.py
   │     │  │  │  ├─ filetypes.py
   │     │  │  │  ├─ glibc.py
   │     │  │  │  ├─ hashes.py
   │     │  │  │  ├─ inject_securetransport.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packaging.py
   │     │  │  │  ├─ parallel.py
   │     │  │  │  ├─ pkg_resources.py
   │     │  │  │  ├─ setuptools_build.py
   │     │  │  │  ├─ subprocess.py
   │     │  │  │  ├─ temp_dir.py
   │     │  │  │  ├─ typing.py
   │     │  │  │  ├─ unpacking.py
   │     │  │  │  ├─ urls.py
   │     │  │  │  ├─ virtualenv.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ appdirs.cpython-38.pyc
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ compatibility_tags.cpython-38.pyc
   │     │  │  │     ├─ datetime.cpython-38.pyc
   │     │  │  │     ├─ deprecation.cpython-38.pyc
   │     │  │  │     ├─ direct_url_helpers.cpython-38.pyc
   │     │  │  │     ├─ distutils_args.cpython-38.pyc
   │     │  │  │     ├─ encoding.cpython-38.pyc
   │     │  │  │     ├─ entrypoints.cpython-38.pyc
   │     │  │  │     ├─ filesystem.cpython-38.pyc
   │     │  │  │     ├─ filetypes.cpython-38.pyc
   │     │  │  │     ├─ glibc.cpython-38.pyc
   │     │  │  │     ├─ hashes.cpython-38.pyc
   │     │  │  │     ├─ inject_securetransport.cpython-38.pyc
   │     │  │  │     ├─ logging.cpython-38.pyc
   │     │  │  │     ├─ misc.cpython-38.pyc
   │     │  │  │     ├─ models.cpython-38.pyc
   │     │  │  │     ├─ packaging.cpython-38.pyc
   │     │  │  │     ├─ parallel.cpython-38.pyc
   │     │  │  │     ├─ pkg_resources.cpython-38.pyc
   │     │  │  │     ├─ setuptools_build.cpython-38.pyc
   │     │  │  │     ├─ subprocess.cpython-38.pyc
   │     │  │  │     ├─ temp_dir.cpython-38.pyc
   │     │  │  │     ├─ typing.cpython-38.pyc
   │     │  │  │     ├─ unpacking.cpython-38.pyc
   │     │  │  │     ├─ urls.cpython-38.pyc
   │     │  │  │     ├─ virtualenv.cpython-38.pyc
   │     │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ vcs
   │     │  │  │  ├─ bazaar.py
   │     │  │  │  ├─ git.py
   │     │  │  │  ├─ mercurial.py
   │     │  │  │  ├─ subversion.py
   │     │  │  │  ├─ versioncontrol.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ bazaar.cpython-38.pyc
   │     │  │  │     ├─ git.cpython-38.pyc
   │     │  │  │     ├─ mercurial.cpython-38.pyc
   │     │  │  │     ├─ subversion.cpython-38.pyc
   │     │  │  │     ├─ versioncontrol.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ wheel_builder.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ build_env.cpython-38.pyc
   │     │  │     ├─ cache.cpython-38.pyc
   │     │  │     ├─ configuration.cpython-38.pyc
   │     │  │     ├─ exceptions.cpython-38.pyc
   │     │  │     ├─ locations.cpython-38.pyc
   │     │  │     ├─ main.cpython-38.pyc
   │     │  │     ├─ pyproject.cpython-38.pyc
   │     │  │     ├─ self_outdated_check.cpython-38.pyc
   │     │  │     ├─ wheel_builder.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ _vendor
   │     │  │  ├─ appdirs.py
   │     │  │  ├─ cachecontrol
   │     │  │  │  ├─ adapter.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ caches
   │     │  │  │  │  ├─ file_cache.py
   │     │  │  │  │  ├─ redis_cache.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ file_cache.cpython-38.pyc
   │     │  │  │  │     ├─ redis_cache.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ controller.py
   │     │  │  │  ├─ filewrapper.py
   │     │  │  │  ├─ heuristics.py
   │     │  │  │  ├─ serialize.py
   │     │  │  │  ├─ wrapper.py
   │     │  │  │  ├─ _cmd.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ adapter.cpython-38.pyc
   │     │  │  │     ├─ cache.cpython-38.pyc
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ controller.cpython-38.pyc
   │     │  │  │     ├─ filewrapper.cpython-38.pyc
   │     │  │  │     ├─ heuristics.cpython-38.pyc
   │     │  │  │     ├─ serialize.cpython-38.pyc
   │     │  │  │     ├─ wrapper.cpython-38.pyc
   │     │  │  │     ├─ _cmd.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ certifi
   │     │  │  │  ├─ cacert.pem
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  ├─ __main__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ core.cpython-38.pyc
   │     │  │  │     ├─ __init__.cpython-38.pyc
   │     │  │  │     └─ __main__.cpython-38.pyc
   │     │  │  ├─ chardet
   │     │  │  │  ├─ big5freq.py
   │     │  │  │  ├─ big5prober.py
   │     │  │  │  ├─ chardistribution.py
   │     │  │  │  ├─ charsetgroupprober.py
   │     │  │  │  ├─ charsetprober.py
   │     │  │  │  ├─ cli
   │     │  │  │  │  ├─ chardetect.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ chardetect.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ codingstatemachine.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ cp949prober.py
   │     │  │  │  ├─ enums.py
   │     │  │  │  ├─ escprober.py
   │     │  │  │  ├─ escsm.py
   │     │  │  │  ├─ eucjpprober.py
   │     │  │  │  ├─ euckrfreq.py
   │     │  │  │  ├─ euckrprober.py
   │     │  │  │  ├─ euctwfreq.py
   │     │  │  │  ├─ euctwprober.py
   │     │  │  │  ├─ gb2312freq.py
   │     │  │  │  ├─ gb2312prober.py
   │     │  │  │  ├─ hebrewprober.py
   │     │  │  │  ├─ jisfreq.py
   │     │  │  │  ├─ jpcntx.py
   │     │  │  │  ├─ langbulgarianmodel.py
   │     │  │  │  ├─ langcyrillicmodel.py
   │     │  │  │  ├─ langgreekmodel.py
   │     │  │  │  ├─ langhebrewmodel.py
   │     │  │  │  ├─ langhungarianmodel.py
   │     │  │  │  ├─ langthaimodel.py
   │     │  │  │  ├─ langturkishmodel.py
   │     │  │  │  ├─ latin1prober.py
   │     │  │  │  ├─ mbcharsetprober.py
   │     │  │  │  ├─ mbcsgroupprober.py
   │     │  │  │  ├─ mbcssm.py
   │     │  │  │  ├─ sbcharsetprober.py
   │     │  │  │  ├─ sbcsgroupprober.py
   │     │  │  │  ├─ sjisprober.py
   │     │  │  │  ├─ universaldetector.py
   │     │  │  │  ├─ utf8prober.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ big5freq.cpython-38.pyc
   │     │  │  │     ├─ big5prober.cpython-38.pyc
   │     │  │  │     ├─ chardistribution.cpython-38.pyc
   │     │  │  │     ├─ charsetgroupprober.cpython-38.pyc
   │     │  │  │     ├─ charsetprober.cpython-38.pyc
   │     │  │  │     ├─ codingstatemachine.cpython-38.pyc
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ cp949prober.cpython-38.pyc
   │     │  │  │     ├─ enums.cpython-38.pyc
   │     │  │  │     ├─ escprober.cpython-38.pyc
   │     │  │  │     ├─ escsm.cpython-38.pyc
   │     │  │  │     ├─ eucjpprober.cpython-38.pyc
   │     │  │  │     ├─ euckrfreq.cpython-38.pyc
   │     │  │  │     ├─ euckrprober.cpython-38.pyc
   │     │  │  │     ├─ euctwfreq.cpython-38.pyc
   │     │  │  │     ├─ euctwprober.cpython-38.pyc
   │     │  │  │     ├─ gb2312freq.cpython-38.pyc
   │     │  │  │     ├─ gb2312prober.cpython-38.pyc
   │     │  │  │     ├─ hebrewprober.cpython-38.pyc
   │     │  │  │     ├─ jisfreq.cpython-38.pyc
   │     │  │  │     ├─ jpcntx.cpython-38.pyc
   │     │  │  │     ├─ langbulgarianmodel.cpython-38.pyc
   │     │  │  │     ├─ langcyrillicmodel.cpython-38.pyc
   │     │  │  │     ├─ langgreekmodel.cpython-38.pyc
   │     │  │  │     ├─ langhebrewmodel.cpython-38.pyc
   │     │  │  │     ├─ langhungarianmodel.cpython-38.pyc
   │     │  │  │     ├─ langthaimodel.cpython-38.pyc
   │     │  │  │     ├─ langturkishmodel.cpython-38.pyc
   │     │  │  │     ├─ latin1prober.cpython-38.pyc
   │     │  │  │     ├─ mbcharsetprober.cpython-38.pyc
   │     │  │  │     ├─ mbcsgroupprober.cpython-38.pyc
   │     │  │  │     ├─ mbcssm.cpython-38.pyc
   │     │  │  │     ├─ sbcharsetprober.cpython-38.pyc
   │     │  │  │     ├─ sbcsgroupprober.cpython-38.pyc
   │     │  │  │     ├─ sjisprober.cpython-38.pyc
   │     │  │  │     ├─ universaldetector.cpython-38.pyc
   │     │  │  │     ├─ utf8prober.cpython-38.pyc
   │     │  │  │     ├─ version.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ colorama
   │     │  │  │  ├─ ansi.py
   │     │  │  │  ├─ ansitowin32.py
   │     │  │  │  ├─ initialise.py
   │     │  │  │  ├─ win32.py
   │     │  │  │  ├─ winterm.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ ansi.cpython-38.pyc
   │     │  │  │     ├─ ansitowin32.cpython-38.pyc
   │     │  │  │     ├─ initialise.cpython-38.pyc
   │     │  │  │     ├─ win32.cpython-38.pyc
   │     │  │  │     ├─ winterm.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ contextlib2.py
   │     │  │  ├─ distlib
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ database.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ locators.py
   │     │  │  │  ├─ manifest.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ resources.py
   │     │  │  │  ├─ scripts.py
   │     │  │  │  ├─ t32.exe
   │     │  │  │  ├─ t64.exe
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ w32.exe
   │     │  │  │  ├─ w64.exe
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ _backport
   │     │  │  │  │  ├─ misc.py
   │     │  │  │  │  ├─ shutil.py
   │     │  │  │  │  ├─ sysconfig.cfg
   │     │  │  │  │  ├─ sysconfig.py
   │     │  │  │  │  ├─ tarfile.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ misc.cpython-38.pyc
   │     │  │  │  │     ├─ shutil.cpython-38.pyc
   │     │  │  │  │     ├─ sysconfig.cpython-38.pyc
   │     │  │  │  │     ├─ tarfile.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ database.cpython-38.pyc
   │     │  │  │     ├─ index.cpython-38.pyc
   │     │  │  │     ├─ locators.cpython-38.pyc
   │     │  │  │     ├─ manifest.cpython-38.pyc
   │     │  │  │     ├─ markers.cpython-38.pyc
   │     │  │  │     ├─ metadata.cpython-38.pyc
   │     │  │  │     ├─ resources.cpython-38.pyc
   │     │  │  │     ├─ scripts.cpython-38.pyc
   │     │  │  │     ├─ util.cpython-38.pyc
   │     │  │  │     ├─ version.cpython-38.pyc
   │     │  │  │     ├─ wheel.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ distro.py
   │     │  │  ├─ html5lib
   │     │  │  │  ├─ constants.py
   │     │  │  │  ├─ filters
   │     │  │  │  │  ├─ alphabeticalattributes.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ inject_meta_charset.py
   │     │  │  │  │  ├─ lint.py
   │     │  │  │  │  ├─ optionaltags.py
   │     │  │  │  │  ├─ sanitizer.py
   │     │  │  │  │  ├─ whitespace.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ alphabeticalattributes.cpython-38.pyc
   │     │  │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │  │     ├─ inject_meta_charset.cpython-38.pyc
   │     │  │  │  │     ├─ lint.cpython-38.pyc
   │     │  │  │  │     ├─ optionaltags.cpython-38.pyc
   │     │  │  │  │     ├─ sanitizer.cpython-38.pyc
   │     │  │  │  │     ├─ whitespace.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ html5parser.py
   │     │  │  │  ├─ serializer.py
   │     │  │  │  ├─ treeadapters
   │     │  │  │  │  ├─ genshi.py
   │     │  │  │  │  ├─ sax.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ genshi.cpython-38.pyc
   │     │  │  │  │     ├─ sax.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ treebuilders
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ dom.py
   │     │  │  │  │  ├─ etree.py
   │     │  │  │  │  ├─ etree_lxml.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │  │     ├─ dom.cpython-38.pyc
   │     │  │  │  │     ├─ etree.cpython-38.pyc
   │     │  │  │  │     ├─ etree_lxml.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ treewalkers
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ dom.py
   │     │  │  │  │  ├─ etree.py
   │     │  │  │  │  ├─ etree_lxml.py
   │     │  │  │  │  ├─ genshi.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ base.cpython-38.pyc
   │     │  │  │  │     ├─ dom.cpython-38.pyc
   │     │  │  │  │     ├─ etree.cpython-38.pyc
   │     │  │  │  │     ├─ etree_lxml.cpython-38.pyc
   │     │  │  │  │     ├─ genshi.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ _ihatexml.py
   │     │  │  │  ├─ _inputstream.py
   │     │  │  │  ├─ _tokenizer.py
   │     │  │  │  ├─ _trie
   │     │  │  │  │  ├─ py.py
   │     │  │  │  │  ├─ _base.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ py.cpython-38.pyc
   │     │  │  │  │     ├─ _base.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ _utils.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ constants.cpython-38.pyc
   │     │  │  │     ├─ html5parser.cpython-38.pyc
   │     │  │  │     ├─ serializer.cpython-38.pyc
   │     │  │  │     ├─ _ihatexml.cpython-38.pyc
   │     │  │  │     ├─ _inputstream.cpython-38.pyc
   │     │  │  │     ├─ _tokenizer.cpython-38.pyc
   │     │  │  │     ├─ _utils.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ idna
   │     │  │  │  ├─ codec.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ idnadata.py
   │     │  │  │  ├─ intranges.py
   │     │  │  │  ├─ package_data.py
   │     │  │  │  ├─ uts46data.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ codec.cpython-38.pyc
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ core.cpython-38.pyc
   │     │  │  │     ├─ idnadata.cpython-38.pyc
   │     │  │  │     ├─ intranges.cpython-38.pyc
   │     │  │  │     ├─ package_data.cpython-38.pyc
   │     │  │  │     ├─ uts46data.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ ipaddress.py
   │     │  │  ├─ msgpack
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ ext.py
   │     │  │  │  ├─ fallback.py
   │     │  │  │  ├─ _version.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ exceptions.cpython-38.pyc
   │     │  │  │     ├─ ext.cpython-38.pyc
   │     │  │  │     ├─ fallback.cpython-38.pyc
   │     │  │  │     ├─ _version.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ _typing.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ markers.cpython-38.pyc
   │     │  │  │     ├─ requirements.cpython-38.pyc
   │     │  │  │     ├─ specifiers.cpython-38.pyc
   │     │  │  │     ├─ tags.cpython-38.pyc
   │     │  │  │     ├─ utils.cpython-38.pyc
   │     │  │  │     ├─ version.cpython-38.pyc
   │     │  │  │     ├─ _compat.cpython-38.pyc
   │     │  │  │     ├─ _structures.cpython-38.pyc
   │     │  │  │     ├─ _typing.cpython-38.pyc
   │     │  │  │     ├─ __about__.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pep517
   │     │  │  │  ├─ build.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ colorlog.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ dirtools.py
   │     │  │  │  ├─ envbuild.py
   │     │  │  │  ├─ meta.py
   │     │  │  │  ├─ wrappers.py
   │     │  │  │  ├─ _in_process.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ build.cpython-38.pyc
   │     │  │  │     ├─ check.cpython-38.pyc
   │     │  │  │     ├─ colorlog.cpython-38.pyc
   │     │  │  │     ├─ compat.cpython-38.pyc
   │     │  │  │     ├─ dirtools.cpython-38.pyc
   │     │  │  │     ├─ envbuild.cpython-38.pyc
   │     │  │  │     ├─ meta.cpython-38.pyc
   │     │  │  │     ├─ wrappers.cpython-38.pyc
   │     │  │  │     ├─ _in_process.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pkg_resources
   │     │  │  │  ├─ py31compat.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ py31compat.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ progress
   │     │  │  │  ├─ bar.py
   │     │  │  │  ├─ counter.py
   │     │  │  │  ├─ spinner.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ bar.cpython-38.pyc
   │     │  │  │     ├─ counter.cpython-38.pyc
   │     │  │  │     ├─ spinner.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pyparsing.py
   │     │  │  ├─ requests
   │     │  │  │  ├─ adapters.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ certs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ cookies.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ hooks.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packages.py
   │     │  │  │  ├─ sessions.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  ├─ structures.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ _internal_utils.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  ├─ __pycache__
   │     │  │  │  │  ├─ adapters.cpython-38.pyc
   │     │  │  │  │  ├─ api.cpython-38.pyc
   │     │  │  │  │  ├─ auth.cpython-38.pyc
   │     │  │  │  │  ├─ certs.cpython-38.pyc
   │     │  │  │  │  ├─ compat.cpython-38.pyc
   │     │  │  │  │  ├─ cookies.cpython-38.pyc
   │     │  │  │  │  ├─ exceptions.cpython-38.pyc
   │     │  │  │  │  ├─ help.cpython-38.pyc
   │     │  │  │  │  ├─ hooks.cpython-38.pyc
   │     │  │  │  │  ├─ models.cpython-38.pyc
   │     │  │  │  │  ├─ packages.cpython-38.pyc
   │     │  │  │  │  ├─ sessions.cpython-38.pyc
   │     │  │  │  │  ├─ status_codes.cpython-38.pyc
   │     │  │  │  │  ├─ structures.cpython-38.pyc
   │     │  │  │  │  ├─ utils.cpython-38.pyc
   │     │  │  │  │  ├─ _internal_utils.cpython-38.pyc
   │     │  │  │  │  ├─ __init__.cpython-38.pyc
   │     │  │  │  │  └─ __version__.cpython-38.pyc
   │     │  │  │  └─ __version__.py
   │     │  │  ├─ resolvelib
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ collections_abc.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ collections_abc.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ providers.py
   │     │  │  │  ├─ reporters.py
   │     │  │  │  ├─ resolvers.py
   │     │  │  │  ├─ structs.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ providers.cpython-38.pyc
   │     │  │  │     ├─ reporters.cpython-38.pyc
   │     │  │  │     ├─ resolvers.cpython-38.pyc
   │     │  │  │     ├─ structs.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ retrying.py
   │     │  │  ├─ six.py
   │     │  │  ├─ toml
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ ordered.py
   │     │  │  │  ├─ tz.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ common.cpython-38.pyc
   │     │  │  │     ├─ decoder.cpython-38.pyc
   │     │  │  │     ├─ encoder.cpython-38.pyc
   │     │  │  │     ├─ ordered.cpython-38.pyc
   │     │  │  │     ├─ tz.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ urllib3
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ connectionpool.py
   │     │  │  │  ├─ contrib
   │     │  │  │  │  ├─ appengine.py
   │     │  │  │  │  ├─ ntlmpool.py
   │     │  │  │  │  ├─ pyopenssl.py
   │     │  │  │  │  ├─ securetransport.py
   │     │  │  │  │  ├─ socks.py
   │     │  │  │  │  ├─ _appengine_environ.py
   │     │  │  │  │  ├─ _securetransport
   │     │  │  │  │  │  ├─ bindings.py
   │     │  │  │  │  │  ├─ low_level.py
   │     │  │  │  │  │  ├─ __init__.py
   │     │  │  │  │  │  └─ __pycache__
   │     │  │  │  │  │     ├─ bindings.cpython-38.pyc
   │     │  │  │  │  │     ├─ low_level.cpython-38.pyc
   │     │  │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ appengine.cpython-38.pyc
   │     │  │  │  │     ├─ ntlmpool.cpython-38.pyc
   │     │  │  │  │     ├─ pyopenssl.cpython-38.pyc
   │     │  │  │  │     ├─ securetransport.cpython-38.pyc
   │     │  │  │  │     ├─ socks.cpython-38.pyc
   │     │  │  │  │     ├─ _appengine_environ.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ fields.py
   │     │  │  │  ├─ filepost.py
   │     │  │  │  ├─ packages
   │     │  │  │  │  ├─ backports
   │     │  │  │  │  │  ├─ makefile.py
   │     │  │  │  │  │  ├─ __init__.py
   │     │  │  │  │  │  └─ __pycache__
   │     │  │  │  │  │     ├─ makefile.cpython-38.pyc
   │     │  │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  │  ├─ six.py
   │     │  │  │  │  ├─ ssl_match_hostname
   │     │  │  │  │  │  ├─ _implementation.py
   │     │  │  │  │  │  ├─ __init__.py
   │     │  │  │  │  │  └─ __pycache__
   │     │  │  │  │  │     ├─ _implementation.cpython-38.pyc
   │     │  │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ six.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ poolmanager.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  ├─ util
   │     │  │  │  │  ├─ connection.py
   │     │  │  │  │  ├─ queue.py
   │     │  │  │  │  ├─ request.py
   │     │  │  │  │  ├─ response.py
   │     │  │  │  │  ├─ retry.py
   │     │  │  │  │  ├─ ssl_.py
   │     │  │  │  │  ├─ timeout.py
   │     │  │  │  │  ├─ url.py
   │     │  │  │  │  ├─ wait.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __pycache__
   │     │  │  │  │     ├─ connection.cpython-38.pyc
   │     │  │  │  │     ├─ queue.cpython-38.pyc
   │     │  │  │  │     ├─ request.cpython-38.pyc
   │     │  │  │  │     ├─ response.cpython-38.pyc
   │     │  │  │  │     ├─ retry.cpython-38.pyc
   │     │  │  │  │     ├─ ssl_.cpython-38.pyc
   │     │  │  │  │     ├─ timeout.cpython-38.pyc
   │     │  │  │  │     ├─ url.cpython-38.pyc
   │     │  │  │  │     ├─ wait.cpython-38.pyc
   │     │  │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ connection.cpython-38.pyc
   │     │  │  │     ├─ connectionpool.cpython-38.pyc
   │     │  │  │     ├─ exceptions.cpython-38.pyc
   │     │  │  │     ├─ fields.cpython-38.pyc
   │     │  │  │     ├─ filepost.cpython-38.pyc
   │     │  │  │     ├─ poolmanager.cpython-38.pyc
   │     │  │  │     ├─ request.cpython-38.pyc
   │     │  │  │     ├─ response.cpython-38.pyc
   │     │  │  │     ├─ _collections.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ vendor.txt
   │     │  │  ├─ webencodings
   │     │  │  │  ├─ labels.py
   │     │  │  │  ├─ mklabels.py
   │     │  │  │  ├─ tests.py
   │     │  │  │  ├─ x_user_defined.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ labels.cpython-38.pyc
   │     │  │  │     ├─ mklabels.cpython-38.pyc
   │     │  │  │     ├─ tests.cpython-38.pyc
   │     │  │  │     ├─ x_user_defined.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ appdirs.cpython-38.pyc
   │     │  │     ├─ contextlib2.cpython-38.pyc
   │     │  │     ├─ distro.cpython-38.pyc
   │     │  │     ├─ ipaddress.cpython-38.pyc
   │     │  │     ├─ pyparsing.cpython-38.pyc
   │     │  │     ├─ retrying.cpython-38.pyc
   │     │  │     ├─ six.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ __init__.py
   │     │  ├─ __main__.py
   │     │  └─ __pycache__
   │     │     ├─ __init__.cpython-38.pyc
   │     │     └─ __main__.cpython-38.pyc
   │     ├─ pip-20.2.3.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pkg_resources
   │     │  ├─ extern
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ _vendor
   │     │  │  ├─ appdirs.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ markers.cpython-38.pyc
   │     │  │  │     ├─ requirements.cpython-38.pyc
   │     │  │  │     ├─ specifiers.cpython-38.pyc
   │     │  │  │     ├─ tags.cpython-38.pyc
   │     │  │  │     ├─ utils.cpython-38.pyc
   │     │  │  │     ├─ version.cpython-38.pyc
   │     │  │  │     ├─ _compat.cpython-38.pyc
   │     │  │  │     ├─ _structures.cpython-38.pyc
   │     │  │  │     ├─ __about__.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pyparsing.py
   │     │  │  ├─ six.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ appdirs.cpython-38.pyc
   │     │  │     ├─ pyparsing.cpython-38.pyc
   │     │  │     ├─ six.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ __init__.py
   │     │  └─ __pycache__
   │     │     └─ __init__.cpython-38.pyc
   │     ├─ setuptools
   │     │  ├─ archive_util.py
   │     │  ├─ build_meta.py
   │     │  ├─ cli-32.exe
   │     │  ├─ cli-64.exe
   │     │  ├─ cli.exe
   │     │  ├─ command
   │     │  │  ├─ alias.py
   │     │  │  ├─ bdist_egg.py
   │     │  │  ├─ bdist_rpm.py
   │     │  │  ├─ bdist_wininst.py
   │     │  │  ├─ build_clib.py
   │     │  │  ├─ build_ext.py
   │     │  │  ├─ build_py.py
   │     │  │  ├─ develop.py
   │     │  │  ├─ dist_info.py
   │     │  │  ├─ easy_install.py
   │     │  │  ├─ egg_info.py
   │     │  │  ├─ install.py
   │     │  │  ├─ install_egg_info.py
   │     │  │  ├─ install_lib.py
   │     │  │  ├─ install_scripts.py
   │     │  │  ├─ launcher manifest.xml
   │     │  │  ├─ py36compat.py
   │     │  │  ├─ register.py
   │     │  │  ├─ rotate.py
   │     │  │  ├─ saveopts.py
   │     │  │  ├─ sdist.py
   │     │  │  ├─ setopt.py
   │     │  │  ├─ test.py
   │     │  │  ├─ upload.py
   │     │  │  ├─ upload_docs.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ alias.cpython-38.pyc
   │     │  │     ├─ bdist_egg.cpython-38.pyc
   │     │  │     ├─ bdist_rpm.cpython-38.pyc
   │     │  │     ├─ bdist_wininst.cpython-38.pyc
   │     │  │     ├─ build_clib.cpython-38.pyc
   │     │  │     ├─ build_ext.cpython-38.pyc
   │     │  │     ├─ build_py.cpython-38.pyc
   │     │  │     ├─ develop.cpython-38.pyc
   │     │  │     ├─ dist_info.cpython-38.pyc
   │     │  │     ├─ easy_install.cpython-38.pyc
   │     │  │     ├─ egg_info.cpython-38.pyc
   │     │  │     ├─ install.cpython-38.pyc
   │     │  │     ├─ install_egg_info.cpython-38.pyc
   │     │  │     ├─ install_lib.cpython-38.pyc
   │     │  │     ├─ install_scripts.cpython-38.pyc
   │     │  │     ├─ py36compat.cpython-38.pyc
   │     │  │     ├─ register.cpython-38.pyc
   │     │  │     ├─ rotate.cpython-38.pyc
   │     │  │     ├─ saveopts.cpython-38.pyc
   │     │  │     ├─ sdist.cpython-38.pyc
   │     │  │     ├─ setopt.cpython-38.pyc
   │     │  │     ├─ test.cpython-38.pyc
   │     │  │     ├─ upload.cpython-38.pyc
   │     │  │     ├─ upload_docs.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ config.py
   │     │  ├─ depends.py
   │     │  ├─ dep_util.py
   │     │  ├─ dist.py
   │     │  ├─ distutils_patch.py
   │     │  ├─ errors.py
   │     │  ├─ extension.py
   │     │  ├─ extern
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ glob.py
   │     │  ├─ gui-32.exe
   │     │  ├─ gui-64.exe
   │     │  ├─ gui.exe
   │     │  ├─ installer.py
   │     │  ├─ launch.py
   │     │  ├─ lib2to3_ex.py
   │     │  ├─ monkey.py
   │     │  ├─ msvc.py
   │     │  ├─ namespaces.py
   │     │  ├─ package_index.py
   │     │  ├─ py27compat.py
   │     │  ├─ py31compat.py
   │     │  ├─ py33compat.py
   │     │  ├─ py34compat.py
   │     │  ├─ sandbox.py
   │     │  ├─ script (dev).tmpl
   │     │  ├─ script.tmpl
   │     │  ├─ ssl_support.py
   │     │  ├─ unicode_utils.py
   │     │  ├─ version.py
   │     │  ├─ wheel.py
   │     │  ├─ windows_support.py
   │     │  ├─ _deprecation_warning.py
   │     │  ├─ _distutils
   │     │  │  ├─ archive_util.py
   │     │  │  ├─ bcppcompiler.py
   │     │  │  ├─ ccompiler.py
   │     │  │  ├─ cmd.py
   │     │  │  ├─ command
   │     │  │  │  ├─ bdist.py
   │     │  │  │  ├─ bdist_dumb.py
   │     │  │  │  ├─ bdist_msi.py
   │     │  │  │  ├─ bdist_rpm.py
   │     │  │  │  ├─ bdist_wininst.py
   │     │  │  │  ├─ build.py
   │     │  │  │  ├─ build_clib.py
   │     │  │  │  ├─ build_ext.py
   │     │  │  │  ├─ build_py.py
   │     │  │  │  ├─ build_scripts.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ clean.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ install_data.py
   │     │  │  │  ├─ install_egg_info.py
   │     │  │  │  ├─ install_headers.py
   │     │  │  │  ├─ install_lib.py
   │     │  │  │  ├─ install_scripts.py
   │     │  │  │  ├─ register.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ upload.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ bdist.cpython-38.pyc
   │     │  │  │     ├─ bdist_dumb.cpython-38.pyc
   │     │  │  │     ├─ bdist_msi.cpython-38.pyc
   │     │  │  │     ├─ bdist_rpm.cpython-38.pyc
   │     │  │  │     ├─ bdist_wininst.cpython-38.pyc
   │     │  │  │     ├─ build.cpython-38.pyc
   │     │  │  │     ├─ build_clib.cpython-38.pyc
   │     │  │  │     ├─ build_ext.cpython-38.pyc
   │     │  │  │     ├─ build_py.cpython-38.pyc
   │     │  │  │     ├─ build_scripts.cpython-38.pyc
   │     │  │  │     ├─ check.cpython-38.pyc
   │     │  │  │     ├─ clean.cpython-38.pyc
   │     │  │  │     ├─ config.cpython-38.pyc
   │     │  │  │     ├─ install.cpython-38.pyc
   │     │  │  │     ├─ install_data.cpython-38.pyc
   │     │  │  │     ├─ install_egg_info.cpython-38.pyc
   │     │  │  │     ├─ install_headers.cpython-38.pyc
   │     │  │  │     ├─ install_lib.cpython-38.pyc
   │     │  │  │     ├─ install_scripts.cpython-38.pyc
   │     │  │  │     ├─ register.cpython-38.pyc
   │     │  │  │     ├─ sdist.cpython-38.pyc
   │     │  │  │     ├─ upload.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ config.py
   │     │  │  ├─ core.py
   │     │  │  ├─ cygwinccompiler.py
   │     │  │  ├─ debug.py
   │     │  │  ├─ dep_util.py
   │     │  │  ├─ dir_util.py
   │     │  │  ├─ dist.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ extension.py
   │     │  │  ├─ fancy_getopt.py
   │     │  │  ├─ filelist.py
   │     │  │  ├─ file_util.py
   │     │  │  ├─ log.py
   │     │  │  ├─ msvc9compiler.py
   │     │  │  ├─ msvccompiler.py
   │     │  │  ├─ spawn.py
   │     │  │  ├─ sysconfig.py
   │     │  │  ├─ text_file.py
   │     │  │  ├─ unixccompiler.py
   │     │  │  ├─ util.py
   │     │  │  ├─ version.py
   │     │  │  ├─ versionpredicate.py
   │     │  │  ├─ _msvccompiler.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ archive_util.cpython-38.pyc
   │     │  │     ├─ bcppcompiler.cpython-38.pyc
   │     │  │     ├─ ccompiler.cpython-38.pyc
   │     │  │     ├─ cmd.cpython-38.pyc
   │     │  │     ├─ config.cpython-38.pyc
   │     │  │     ├─ core.cpython-38.pyc
   │     │  │     ├─ cygwinccompiler.cpython-38.pyc
   │     │  │     ├─ debug.cpython-38.pyc
   │     │  │     ├─ dep_util.cpython-38.pyc
   │     │  │     ├─ dir_util.cpython-38.pyc
   │     │  │     ├─ dist.cpython-38.pyc
   │     │  │     ├─ errors.cpython-38.pyc
   │     │  │     ├─ extension.cpython-38.pyc
   │     │  │     ├─ fancy_getopt.cpython-38.pyc
   │     │  │     ├─ filelist.cpython-38.pyc
   │     │  │     ├─ file_util.cpython-38.pyc
   │     │  │     ├─ log.cpython-38.pyc
   │     │  │     ├─ msvc9compiler.cpython-38.pyc
   │     │  │     ├─ msvccompiler.cpython-38.pyc
   │     │  │     ├─ spawn.cpython-38.pyc
   │     │  │     ├─ sysconfig.cpython-38.pyc
   │     │  │     ├─ text_file.cpython-38.pyc
   │     │  │     ├─ unixccompiler.cpython-38.pyc
   │     │  │     ├─ util.cpython-38.pyc
   │     │  │     ├─ version.cpython-38.pyc
   │     │  │     ├─ versionpredicate.cpython-38.pyc
   │     │  │     ├─ _msvccompiler.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ _imp.py
   │     │  ├─ _vendor
   │     │  │  ├─ ordered_set.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __pycache__
   │     │  │  │     ├─ markers.cpython-38.pyc
   │     │  │  │     ├─ requirements.cpython-38.pyc
   │     │  │  │     ├─ specifiers.cpython-38.pyc
   │     │  │  │     ├─ tags.cpython-38.pyc
   │     │  │  │     ├─ utils.cpython-38.pyc
   │     │  │  │     ├─ version.cpython-38.pyc
   │     │  │  │     ├─ _compat.cpython-38.pyc
   │     │  │  │     ├─ _structures.cpython-38.pyc
   │     │  │  │     ├─ __about__.cpython-38.pyc
   │     │  │  │     └─ __init__.cpython-38.pyc
   │     │  │  ├─ pyparsing.py
   │     │  │  ├─ six.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pycache__
   │     │  │     ├─ ordered_set.cpython-38.pyc
   │     │  │     ├─ pyparsing.cpython-38.pyc
   │     │  │     ├─ six.cpython-38.pyc
   │     │  │     └─ __init__.cpython-38.pyc
   │     │  ├─ __init__.py
   │     │  └─ __pycache__
   │     │     ├─ archive_util.cpython-38.pyc
   │     │     ├─ build_meta.cpython-38.pyc
   │     │     ├─ config.cpython-38.pyc
   │     │     ├─ depends.cpython-38.pyc
   │     │     ├─ dep_util.cpython-38.pyc
   │     │     ├─ dist.cpython-38.pyc
   │     │     ├─ distutils_patch.cpython-38.pyc
   │     │     ├─ errors.cpython-38.pyc
   │     │     ├─ extension.cpython-38.pyc
   │     │     ├─ glob.cpython-38.pyc
   │     │     ├─ installer.cpython-38.pyc
   │     │     ├─ launch.cpython-38.pyc
   │     │     ├─ lib2to3_ex.cpython-38.pyc
   │     │     ├─ monkey.cpython-38.pyc
   │     │     ├─ msvc.cpython-38.pyc
   │     │     ├─ namespaces.cpython-38.pyc
   │     │     ├─ package_index.cpython-38.pyc
   │     │     ├─ py27compat.cpython-38.pyc
   │     │     ├─ py31compat.cpython-38.pyc
   │     │     ├─ py33compat.cpython-38.pyc
   │     │     ├─ py34compat.cpython-38.pyc
   │     │     ├─ sandbox.cpython-38.pyc
   │     │     ├─ ssl_support.cpython-38.pyc
   │     │     ├─ unicode_utils.cpython-38.pyc
   │     │     ├─ version.cpython-38.pyc
   │     │     ├─ wheel.cpython-38.pyc
   │     │     ├─ windows_support.cpython-38.pyc
   │     │     ├─ _deprecation_warning.cpython-38.pyc
   │     │     ├─ _imp.cpython-38.pyc
   │     │     └─ __init__.cpython-38.pyc
   │     ├─ setuptools-49.2.1.dist-info
   │     │  ├─ dependency_links.txt
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     └─ __pycache__
   │        └─ easy_install.cpython-38.pyc
   ├─ pyvenv.cfg
   └─ Scripts
      ├─ activate
      ├─ activate.bat
      ├─ Activate.ps1
      ├─ deactivate.bat
      ├─ easy_install-3.8.exe
      ├─ easy_install.exe
      ├─ pip.exe
      ├─ pip3.8.exe
      ├─ pip3.exe
      ├─ python.exe
      └─ pythonw.exe

```