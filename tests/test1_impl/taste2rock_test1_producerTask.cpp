/* Generated from orogen/lib/orogen/templates/tasks/Task.cpp */

#include "taste2rock_test1_producerTask.hpp"

#include <rtt/OperationCaller.hpp>
#include <rtt/transports/corba/TaskContextProxy.hpp>



using namespace taste2rock_test1_producer;

taste2rock_test1_producerTask::taste2rock_test1_producerTask(std::string const& name, TaskCore::TaskState initial_state)
    : taste2rock_test1_producerTaskBase(name, initial_state)
    , m_vector(0.0, 0.0, 0.0)
    , m_count(0)
    , consumer_getUnprot(NULL)
    , consumer_setProt(NULL)
    , consumer_connected(false)

{
}

taste2rock_test1_producerTask::taste2rock_test1_producerTask(std::string const& name, RTT::ExecutionEngine* engine, TaskCore::TaskState initial_state)
    : taste2rock_test1_producerTaskBase(name, engine, initial_state)
    , m_vector(0.0, 0.0, 0.0)
    , m_count(0)
    , consumer_getUnprot(NULL)
    , consumer_setProt(NULL)
    , consumer_connected(false)
{
}

taste2rock_test1_producerTask::~taste2rock_test1_producerTask()
{
}



/// The following lines are template definitions for the various state machine
// hooks defined by Orocos::RTT. See taste2rock_test1_producerTask.hpp for more detailed
// documentation about them.

bool taste2rock_test1_producerTask::configureHook()
{
    if (! taste2rock_test1_producerTaskBase::configureHook())
        return false;

    RTT::TaskContext *pTask = RTT::corba::TaskContextProxy::Create("taste2rock_test1_consumerTask");
    if (NULL != pTask)
    {
        if (addPeer(pTask))
        {
            consumer_getUnprot = new RTT::OperationCaller< boost::uint32_t() >(pTask->getOperation("getUnprot"));
            consumer_setProt = new RTT::OperationCaller< void(boost::uint32_t) >(pTask->getOperation("setProt"));
            consumer_connected = true;
        }
    }
    if (!consumer_connected)
    {
        std::cerr << "[producer] error connecting consumer operations" << std::endl;
    }

    return true;
}
bool taste2rock_test1_producerTask::startHook()
{
    if (! taste2rock_test1_producerTaskBase::startHook())
        return false;
    return true;
}

void taste2rock_test1_producerTask::updateHook()
{
    taste2rock_test1_producerTaskBase::updateHook();


    boost::int32_t trigger;
    if (RTT::NewData == _taste2rock_test1_producerActivatorTrigger.read(trigger))
    {
        std::cout << "[producer] trigger received" << std::endl;

        if (m_count % 2)
        {
            m_vector = base::Vector3d(m_count, m_count, m_count);
            std::cout << "[producer] send vector (" << m_vector[0] << ", " << m_vector[1] << ", " << m_vector[2] << ")" << std::endl;
            _sendSporadic.write(m_vector);

            if (NULL != consumer_getUnprot)
            {
                boost::uint32_t read = (*consumer_getUnprot)();
                std::cout << "[producer] read count " << read << std::endl;
            }
        }
        else
        {
            boost::int32_t dummy = 0;
            std::cout << "[producer] send empty" << std::endl;
            _sendEmpty.write(dummy);
            
            if (NULL != consumer_setProt)
            {
                std::cout << "[producer] set count " << m_count << std::endl;
                (*consumer_setProt)(m_count);
            }
        }

        m_count++;
    }
}

void taste2rock_test1_producerTask::errorHook()
{
    taste2rock_test1_producerTaskBase::errorHook();
}
void taste2rock_test1_producerTask::stopHook()
{
    taste2rock_test1_producerTaskBase::stopHook();
}
void taste2rock_test1_producerTask::cleanupHook()
{
    taste2rock_test1_producerTaskBase::cleanupHook();
}
