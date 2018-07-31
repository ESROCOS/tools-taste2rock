/* Generated from orogen/lib/orogen/templates/tasks/Task.cpp */

#include "taste2rock_test1_producerActivatorTask.hpp"

using namespace taste2rock_test1_producer;

taste2rock_test1_producerActivatorTask::taste2rock_test1_producerActivatorTask(std::string const& name, TaskCore::TaskState initial_state)
    : taste2rock_test1_producerActivatorTaskBase(name, initial_state)
{
}

taste2rock_test1_producerActivatorTask::taste2rock_test1_producerActivatorTask(std::string const& name, RTT::ExecutionEngine* engine, TaskCore::TaskState initial_state)
    : taste2rock_test1_producerActivatorTaskBase(name, engine, initial_state)
{
}

taste2rock_test1_producerActivatorTask::~taste2rock_test1_producerActivatorTask()
{
}



/// The following lines are template definitions for the various state machine
// hooks defined by Orocos::RTT. See taste2rock_test1_producerActivatorTask.hpp for more detailed
// documentation about them.

bool taste2rock_test1_producerActivatorTask::configureHook()
{
    if (! taste2rock_test1_producerActivatorTaskBase::configureHook())
        return false;
    return true;
}
bool taste2rock_test1_producerActivatorTask::startHook()
{
    if (! taste2rock_test1_producerActivatorTaskBase::startHook())
        return false;
    return true;
}

void taste2rock_test1_producerActivatorTask::updateHook()
{
    taste2rock_test1_producerActivatorTaskBase::updateHook();

    boost::int32_t dummy = 0;
    std::cout << "[producer] activator trigger" << std::endl;
    _taste2rock_test1_producerActivatorTrigger.write(dummy);
}

void taste2rock_test1_producerActivatorTask::errorHook()
{
    taste2rock_test1_producerActivatorTaskBase::errorHook();
}
void taste2rock_test1_producerActivatorTask::stopHook()
{
    taste2rock_test1_producerActivatorTaskBase::stopHook();
}
void taste2rock_test1_producerActivatorTask::cleanupHook()
{
    taste2rock_test1_producerActivatorTaskBase::cleanupHook();
}
