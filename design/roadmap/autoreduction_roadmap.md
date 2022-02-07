# Autoreduction Roadmap

The following is an outline of long term technical improvements to the ISIS Autoreduction service.

Apart from where there are listed dependencies, work items are listed in approximate order of priority weighted on the following criteria:

- Cost/Benefit: smaller, "quick wins" that address sustainability issues are preferred
- External blocking dependencies: work without external dependencies is preferred

Time estimates are given in terms of a FTE Band D developer.

## Move to Kafka as message broker

Current state:

- ActiveMQ is used as transport between components of the Autoreduction system.

Summary of work:

- Deploy a Red Panda message broker.
  Red Panda is a higher performance, easier to manage alternative to the Apace Kafka broker.
- Replace use of ActiveMQ with Kafka in existing Autoreduction components.

Benefits:

- Kafka has features that could be used later on to simplify the architecture of the entire Autoreduction system.
  See "Remove database" item.
- Kafka is a more flexible data transport system, and as such is seeing increasing use within ISIS.
  Standardising on a common technology for a given problem should be sought where possible.

Estimate: 4 months

## Remove database

Current state:

- Historical and current state of reduction jobs is stored in a MySql database.
- The web application backend accesses this database as required.

Summary of work:

- Based on user requirements and the ISIS data policy, determine a data retention policy in order to limit the historic data expected to be kept within Autoreduction.
- Rework message passing to ensure a logical format for Kafka persistence.
- Provision appropriate storage for Red Panda broker.
- Remove separate MySQL database.

Benefits:

- Removes number of components, therefore overall complexity, in overall system architecture.
- Reduces complexity of components that are required to interact with persistent storage by combining this with data transfer operations, rather than having to handle data transfer and persistent storage separately.

Dependencies:

- Move to Kafka as message broker.

Estimate: 6 months

## Rewrite webapp

Current state:

- The current web app is written in Python using the Django framework.
- The code base has changed hands several times throughout its life and has accumulated significant technical debt.

Summary of work:

- Perform a survey of appropriate technologies.
  Given the fast rate that web technologies evolve, some time should be taken at the start of this work to select an appropriate technology stack.
  The technologies used and produced in other STFC departments (e.g. ISIS Facility Business Systems, SCD Data & Software Engineering Group) should also be taken into consideration.
- Rewrite the web app using the chosen technology stack.

Benefits:

- Repays accumulated technical debt.
- Increases standardisation between STFC software groups.
- Provides an opportunity to address user experience issues raised by users of the service.

Estimate: 10 months

## Kubernetes deployment

Current state:

- Autoreduction is deployed on a fixed set of virtual and physical Linux machines managed by the SCD Cloud and ISIS respectively.
- The deployment is managed via Ansible to aid in reproducibility and configuration/change management

Summary of work:

- Containerise all components of Autorduction service.
- Deploy and scale via Kubernetes.

Benefits:

- Increased separation between components and underlying infrastructure further increases reproducibility of deployments.
- Scaling service to match current demand is trivial using native Kubernetes functionality.
- Manintaining multiple deployments is easier.
  This allows isolated development environments, A/B testing and safer deployments of new versions.

Dependencies:

- A on premise Kuberenetes as a service offering.
  Provided by either SCD or ISIS.

Estimate: 8 months

## Generic processing environments

Current state:

- A single, pre-determined environment is provided which must be used for all reduction jobs Autoreduction performs.
  The main component of this environment is Mantid.

Summary of work:

- Provide a means for arbitrary environments to be used, allowing the available tools to be tailored to the specific reduction being performed.
  The specifics of how this is implemented will need to be investigated first, taking into account requirements of data processing not currently performed on Autoreduction.
- Create suitable environments for Autoreduction's existing use cases.

Benefits:

- Provided flexibility of available data treatment software.
- Improves ability to truly reproduce results by tightly controlling versions of available software.
- Allows adoption of Autoreduction by scientific technique areas that cannot use the tools available in the current environment or require additional tools (e.g. neutron imaging).

Estimate: 8 months

## Alternative job submission method(s)

Current state:

- Reduction jobs are triggered by a system that monitors files written by the data archiving system.

Summary of work:

- Investigate the possibility of having the controls/data archive system indicate run completion via Kafka.
  This will require collaboration with the experiment controls group within ISIS.
  The question of where the broker for these messages should be hosted should be addressed, this data could be of use to more than just Autoreduction.
- Replace the existing job trigger within Autoreduction with a trigger that is activated by an appropriate Kafka message.

Benefits:

- Removes the dependency on a legacy system.
- Allows job triggering by a number of external events.
  This could be useful for alternative job triggering modes, e.g. when a selection of pre-defined runs have been completed.

Dependencies:

- Move to Kafka as message broker.
- Provision of a Kafka broker for message delivery.
- Suitable messages being sent from the instrument control system.

Estimate: 6 months

## Jupyter Notebooks

Current state:

- Results of Autoreduction jobs are displayed in the web app, offering log output and basic plotting.
  The only further interaction available is resubmission of the job.

Summary of work:

- Investigate the possibility of using Juptyer Notebooks as an alternative to plain Python scripts for Autoreduction jobs.
- Provide a means of configuring a job in terms of a Jupyter Notebook and accessing the results via an executed notebook running in a Juptyer Lab instance.
- Conversion of existing workflows to Jupyter Notebooks.

Benefits:

- Vastly more flexible user interaction with processed data.
- Reduces complexity of Autoreduction web app.

Dependencies:

- A JupyterLab instance to host the generated notebooks.
  This location will need the same access to data as the Autoreduction compute infrastructure, using the JuptyerLab instance as the Autoreduction compute backend may simplify this.

Estimate: 12 months
