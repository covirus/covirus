from datetime import datetime
import matplotlib.pyplot as plt


class Plotable:
    def plot(self, x_name=None, y_name=None, legend=None, save=False):
        ax = self.initialize_plot()
        ax = self.plot_model(ax)
        ax = self.format_plot(ax, x_name, y_name, legend)
        if save:
            self.save_fig()
        plt.show()

    def initialize_plot(self):
        fig = plt.figure(facecolor="w")
        ax = fig.add_subplot(111, axisbelow=True)
        return ax

    def format_plot(self, ax, x_name, y_name, legend):
        ax = self.set_base_plot_settings(ax)
        if x_name and y_name:
            ax = self.set_axes(ax, x_name, y_name)
        if legend:
            ax = self.set_legend(ax, legend)
        return ax

    def set_axes(self, ax, x_name, y_name):
        self.set_axes_labels(ax, x_name, y_name)
        ax.set_ylim(0, 1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        return ax

    def set_axes_labels(self, ax, x, y):
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        return ax

    def set_base_plot_settings(self, ax):
        ax.grid(b=True, which="major", c="w", lw=2, ls="-")
        for spine in ("top", "right", "bottom", "left"):
            ax.spines[spine].set_visible(False)
        return ax

    def set_legend(self, ax, legend):
        legend = ax.legend(legend)
        legend.get_frame().set_alpha(0.5)

    def save_fig(self):
        filename = f"/{self.model_name}-generated-{datetime.today().date()}.jpg"
        plt.savefig(filename)
