var myHeading = document.getElementById('type');
myHeading.textContent = '目前身份：学生';
function type1()
{
    myHeading.textContent = '目前身份：学生';
}
function type2()
{
    myHeading.textContent = '目前身份：评委';
}
function type3()
{
    myHeading.textContent = '目前身份：队伍管理员';
}
function type4()
{
    myHeading.textContent = '目前身份：平台管理员';
}
 // 定义按钮btn
var btn = document.getElementById('send-vertifycode');
// 定义发送时间间隔(s)
var SEND_INTERVAL = 60;
var timeLeft = SEND_INTERVAL;

/**
* 绑定btn按钮的监听事件
*/
var bindBtn = function(){
    btn.click(function(){
        // 需要先禁用按钮（为防止用户重复点击）
        btn.unbind('click');
        btn.attr('disabled', 'disabled');
        $.ajax({
            // ajax接口调用...
        })
        .done(function () {
            alert('发送成功');
            //成功
            timeLeft = SEND_INTERVAL;
            timeCount();                
        })
        .fail(function () {
            //失败，弹窗
            alert('发送失败');
            // ** 重要：因为发送失败，所以要恢复发送按钮的监听 **
            bindBtn();
            btn.remove('disabled');
        });
    })
}           
/**
* 重新发送计时
**/ 
var timeCount = function() {
    window.setTimeout(function() {
        if(timeLeft > 0) {
            timeLeft -= 1;
            btn.html(timeLeft + "后重新发送");
            timeCount();
        } else {
            btn.html("重新发送");
            bindBtn();
        }
    }, 1000);
}