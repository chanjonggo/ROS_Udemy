#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node
{
public:
    MyNode() : Node("cpp_test")
    {
        timer = this->create_wall_timer(
            std::chrono::seconds(1)
            //, std::bind(&MyNode::timerCallback, this)
            ,[this]() {
                this->timerCallback();
            }
        );
    }
    virtual ~MyNode() = default;

private:
    void timerCallback()
    {
        RCLCPP_INFO( this->get_logger(), "Hello class World %d", counter );
        counter ++;
    }
    rclcpp::TimerBase::SharedPtr timer;
    int32_t counter = 0;
};



int main(int argc, char** argv)
{
    //start 
    rclcpp::init(argc, argv);

    //auto node = std::make_shared<rclcpp::Node>("my_first_node");
    //RCLCPP_INFO( node->get_logger(), "Hello World" );
    auto node = std::make_shared<MyNode>();

    rclcpp::spin(node);

    //end
    rclcpp::shutdown();
    return 0;
}