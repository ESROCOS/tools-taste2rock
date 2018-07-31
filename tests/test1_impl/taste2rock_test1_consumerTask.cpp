/* Generated from orogen/lib/orogen/templates/tasks/Task.cpp */

#include "taste2rock_test1_consumerTask.hpp"

using namespace taste2rock_test1_consumer;

taste2rock_test1_consumerTask::taste2rock_test1_consumerTask(std::string const& name, TaskCore::TaskState initial_state)
    : taste2rock_test1_consumerTaskBase(name, initial_state)
    , m_count(0)
{
}

taste2rock_test1_consumerTask::taste2rock_test1_consumerTask(std::string const& name, RTT::ExecutionEngine* engine, TaskCore::TaskState initial_state)
    : taste2rock_test1_consumerTaskBase(name, engine, initial_state)
    , m_count(0)
{
}

taste2rock_test1_consumerTask::~taste2rock_test1_consumerTask()
{
}

boost::uint32_t taste2rock_test1_consumerTask::getUnprot()
{
    std::cout << "[consumer] queried count " << m_count << std::endl;
    return m_count;
}

void taste2rock_test1_consumerTask::setProt(boost::uint32_t arg)
{
    std::cout << "[consumer] got count " << arg << std::endl;
    m_count = arg;
}

/// The following lines are template definitions for the various state machine
// hooks defined by Orocos::RTT. See taste2rock_test1_consumerTask.hpp for more detailed
// documentation about them.

bool taste2rock_test1_consumerTask::configureHook()
{
    if (! taste2rock_test1_consumerTaskBase::configureHook())
        return false;
        
    return true;
}
bool taste2rock_test1_consumerTask::startHook()
{
    if (! taste2rock_test1_consumerTaskBase::startHook())
        return false;
    return true;
}

void taste2rock_test1_consumerTask::updateHook()
{
    taste2rock_test1_consumerTaskBase::updateHook();

    boost::int32_t dummy;
    base::Vector3d vector;

    if (RTT::NewData == _sendEmpty.read(dummy))
    {
        std::cout << "[consumer] got empty message" << std::endl;
    }
    
    if (RTT::NewData == _sendSporadic.read(vector))
    {
        std::cout << "[consumer] got vector (" << vector[0] << ", " << vector[1] << ", " << vector[2] << ")" << std::endl;
    }
}

void taste2rock_test1_consumerTask::errorHook()
{
    taste2rock_test1_consumerTaskBase::errorHook();
}
void taste2rock_test1_consumerTask::stopHook()
{
    taste2rock_test1_consumerTaskBase::stopHook();
}
void taste2rock_test1_consumerTask::cleanupHook()
{
    taste2rock_test1_consumerTaskBase::cleanupHook();
}
