import pulumi_random
import pulumi


class GoodPasswordArgs:
    def __init__(self):
        pass


class GoodPassword(pulumi.ComponentResource):
    def __init__(self, name_me, opts=None):
        super().__init__('core:index:GoodPassword', name_me, {}, opts)
        child_opts = pulumi.ResourceOptions(parent=self)

        self.password = pulumi_random.RandomPassword(
            f'pwd-{name_me}',
            args=pulumi_random.RandomPasswordArgs(
                keepers={'name': name_me},
                min_lower=3,
                min_numeric=2,
                min_special=1,
                length=12
            ),
            opts=pulumi.ResourceOptions(
                parent=self
            )
        )
        # We also need to register all the expected outputs for this component resource that will get returned by default.
        self.register_outputs({
            "pwd": self.password.result
        })


__all__ = (
    'GoodPassword'
)
