#include <linux/module.h>
#include <linux/fs.h>
#include <linux/init.h>

#define DEVICE_NAME "sample"
static int major;

/* File operations prototypes */
static int device_open(struct inode *inode, struct file *file) {
    pr_info("sample: device opened\n");
    return 0;
}

static int device_release(struct inode *inode, struct file *file) {
    pr_info("sample: device closed\n");
    return 0;
}

static ssize_t device_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
    pr_info("sample: read called\n");
    return 0;
}

static ssize_t device_write(struct file *file, const char __user *buf, size_t len, loff_t *offset) {
    pr_info("sample: write called\n");
    return len;
}

/* File operations structure */
static const struct file_operations fops = {
    .owner = THIS_MODULE,
    .read = device_read,
    .write = device_write,
    .open = device_open,
    .release = device_release,
};

/* Module init function */
static int __init sample_init(void) {
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0) {
        pr_alert("sample: registering char device failed with %d\n", major);
        return major;
    }
    pr_info("sample: registered with major number %d\n", major);
    return 0;
}

/* Module exit function */
static void __exit sample_exit(void) {
    if (major > 0) {
        unregister_chrdev(major, DEVICE_NAME);
        pr_info("sample: unregistered device with major number %d\n", major);
    }
}

module_init(sample_init);
module_exit(sample_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("Sample Linux Character Device Driver");
