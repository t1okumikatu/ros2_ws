// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/robot_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_RobotCommand_Request_dist
{
public:
  Init_RobotCommand_Request_dist()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::RobotCommand_Request dist(::robot_interfaces::srv::RobotCommand_Request::_dist_type arg)
  {
    msg_.dist = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::RobotCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::RobotCommand_Request>()
{
  return robot_interfaces::srv::builder::Init_RobotCommand_Request_dist();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_RobotCommand_Response_done
{
public:
  Init_RobotCommand_Response_done()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::RobotCommand_Response done(::robot_interfaces::srv::RobotCommand_Response::_done_type arg)
  {
    msg_.done = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::RobotCommand_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::RobotCommand_Response>()
{
  return robot_interfaces::srv::builder::Init_RobotCommand_Response_done();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_
